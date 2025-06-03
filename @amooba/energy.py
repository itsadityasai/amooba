# energy range : 1 - 100

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

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

    if (newEnergyVal < 1):
        raise InvalidEnergyErr

    __setEnergy(_id, newEnergyVal)
    return newEnergyVal

def increaseEnergy(_id, amount) -> int:

    newEnergyVal = getEnergy(_id) + amount

    if (newEnergyVal > 100):
        raise InvalidEnergyErr

    __setEnergy(_id, newEnergyVal)

    return newEnergyVal

def needsEnergy(_id) -> bool:
    e = getEnergy(_id)

    if e > 60:
        return False
    else:
        return True
