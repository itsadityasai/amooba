# am : seeing how to solve the dying out problem ; currently testing whether not having two kids at a time helps any
# now : re-make db & start.py --all <-- do this
# if that doesn't work : see line 72

#RESULTS for the parentkey test with isHorny() having a 1:3 chance (no:yes):
# CAN EAT SIBLINGS AND PARENTS BUT NOT CHILDREN: ends with a more-or-less constant 9 organisms left (these 9 change but there's always around 9)
# CAN'T EAT SIBLIGS, PARENTS OR CHILDREN : #same result as above (9 constant left) #on second run stagnated at 5 constant

# graph of growth of numeber of amoobae
#from the graphs, we see that the decline starts at ~150 seconds in

# now trying isHorny() always true - AGAIN, IT'S DECLINING AT ~150s

# OKAY NICE. Setting a default energy value for the child fixes the problem. Now how do we stop it from rising infinitely?
# - change the energy value to a lower once
# OR make less horny


import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

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
    child['energy'] = 100

    while True:
        try:
            db.systems.insert_one(child)
            break
        except pymongo.errors.DuplicateKeyError:
            child['_id'] += 1

    db.env.update_one(
        {'object': None},
        {'$set': {'object': f'amooba{child["_id"]}'}}
    )

    depleteEnergy(parent_id, 50)
    __startNewOrganism(child['_id'])

    return child['_id']

# r = {'True':0, 'False':0}
#
# for i in range(10000):
#     r[str(isHorny())] += 1
#
# print(r)

# no:yes
# 1:1 - neverending (to my knowledge) with just a few survivors keeping it going
# 2:1 - reached a sorta standstill with 2 remaining (excluding 0), just walking through the map.
        # one would've died due to energy loss while hunting or being eaten, and the other would soon follow due to energy loss (there wasn't enough energy to be passed on so the living one would reproduce)
# 1:2 - same result as 2:1
# 1:3 - first time gave the same result as 1:1 - second time it ended with just 1 survivor (who would've died due to energy loss while hunting since there wasn't anyone left to eat)
# 0:1 (return True) - ah fuck, this ended with the same result as 2:!

# so we can conclude that isHorny() is not the problem

# the problem may be that they all start feeding/reproducing at once
# movment energy loss too little?
# 90-10 the problem? - I don't think the organisms were dying out before I started using this system
# what if the problem is that parents r eating their babies?
# if that doesn't fix it then let's raise the energy passed on to the next trophic level
