# for now, moving is like teleporting

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from GLOBALS import *


logfile = None


def goto(_id, new_location) -> bool: #new_location is an ARRAY NOT A TUPLE

    from energy import depleteEnergy
    from plane import __distance
    from sys import exit as die
    import console
    from datetime import datetime

    global logfile

    try:
        original_location = db.env.find_one({'object': f'amooba{int(_id)}'})['point']
    except TypeError:
        console.error(f'[{str(datetime.now())}] movement.goto(): amooba{_id} is dead')
        die()

    x = db.env.find_one({'point': new_location})
    if x['object'] != None:
        return False
    else:
        db.env.update_one(
            {'point': new_location},
            {'$set': {'object': f'amooba{_id}'}}
        )
        db.env.update_one(
            {'point': original_location},
            {'$set': {'object': None}}
        )
        depleteEnergy(
            _id,
            __distance(original_location, new_location) / ENERGY_MOVEMENT_DROP
        )
        logfile.write(f"{_id}:{original_location}:{new_location}\n")
        return True
