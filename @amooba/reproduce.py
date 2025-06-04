import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from GLOBALS import *


def getLatestAmooba():
    rec = db.systems.find(sort=[("_id", -1)]).limit(1) # descending order sort
    return rec[0]['_id']

def getParent(_id):
    rec = db.systems.find_one({'_id':_id})
    if rec is None: #organism died while this function was being called
        return 0 # 0 isn't an active organsim (it's kinda a template organism), and seeing as all other modules handle dead organisms in some way this shouldn't cause any problems
    return rec['parent'].replace('amooba', '')


def canReproduce(_id):
    from energy import getEnergy, needsEnergy

    if (needsEnergy(_id)):
        return False
    else:
        return True

def __startNewOrganism(new_organism_id):
    from subprocess import Popen
    Popen(f'python start.py --one {new_organism_id}', shell=True)


def reproduce(parent_id): # does not check if canReproduce()

    from energy import depleteEnergy
    from sys import exit as die
    import console
    from datetime import datetime

    amooba_to_create = getLatestAmooba() + 1
    parent = db.systems.find_one({"_id" : parent_id})

    if parent is None:
        console.error(f'[{str(datetime.now())}] reproduce.reproduce(): amooba{parent_id} died while reproducing')
        die()

    child = parent
    child['_id'] = amooba_to_create
    child['parent'] = f'amooba{parent_id}'
    child['energy'] = CHILD_SPAWN_ENERGY

    while True:
        try:
            db.systems.insert_one(child)
            break
        except pymongo.errors.DuplicateKeyError:
            child['_id'] += 1

    try:
        random_point = db.env.aggregate([
            { '$match': { 'object': None } },
            { '$sample': { 'size': 1 } }
        ]).next()

        db.env.update_one(
            { '_id': random_point['_id'] },
            { '$set': { 'object': f'amooba{child["_id"]}' } }
        )
    except StopIteration:
        console.error("No empty space to place new amooba!")


    depleteEnergy(parent_id, PARENT_ENERGY_DROP)
    __startNewOrganism(child['_id'])

    return child['_id']
