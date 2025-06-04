import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from GLOBALS import *


class InvalidEnergyErr(Exception):
    pass

def getEnergy(_id) -> int:
    try:
        record = db.systems.find_one({"_id":_id})
        return record['energy']
    except TypeError: # if called on a dead/non-existent organism
        return 0 #this way I don't have to handle None all the time

def __setEnergy(_id, e):
    db.systems.update_one(
        {'_id':_id}, {'$set' : {'energy': e}}
    )

def depleteEnergy(_id, amount) -> int:

    newEnergyVal = getEnergy(_id) - amount

    if (newEnergyVal < MIN_ENERGY_VAL):
        raise InvalidEnergyErr

    __setEnergy(_id, newEnergyVal)
    return newEnergyVal

def increaseEnergy(_id, amount) -> int:

    newEnergyVal = getEnergy(_id) + amount

    if (newEnergyVal > MAX_ENERGY_VAL):
        raise InvalidEnergyErr

    __setEnergy(_id, newEnergyVal)

    return newEnergyVal

def needsEnergy(_id) -> bool:
    e = getEnergy(_id)

    if e > NEW_ENERGY_VAL:
        return False
    else:
        return True
