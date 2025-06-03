# no two objects can lie at one point on the plane
# this plane is a 1001x1001 grid, with a total of 1002001 locations

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

def whereIs(_id) -> list:
    x = db.env.find_one({"object": f"amooba{_id}"})
    try:
        return x['point']
    except TypeError:
        return None

def __distance(a, b):

    x1 = a[0]
    y1 = a[1]

    x2 = b[0]
    y2 = b[1]

    from math import sqrt

    return sqrt(

    	pow(x2 - x1, 2)
    	+ pow(y2-y1, 2)

    )

def getNearbyObjects(nearwhom): # includes nearwhom

    from sys import exit as die
    import console
    from datetime import datetime

    iAmAt = whereIs(nearwhom)
    if iAmAt is None:
        console.error(f'[{str(datetime.now())}] plane.getNearbyObjects(): amooba{nearwhom} is dead')
        die()
    x = int(iAmAt[0])
    y = int(iAmAt[1])
    nearby_coords = []
    for cx in range(x - 5, x + 6, 1):
        for cy in range(y - 5, y + 6, 1):
            nearby_coords.append([cx, cy])
    r = db.env.find(
        {
            "point" : {
                "$in" : nearby_coords
            }
        }
    )
    return list(r)

def get_nearby_amoobae(nearwhom): # does not include nearwhom
    nearby_objects = getNearbyObjects(nearwhom)
    prey_nearby = []
    for _object in nearby_objects:
        if _object['object'] != None and _object['object'] != f"amooba{nearwhom}":
            if _object['object'].startswith('amooba'):
                prey_nearby.append(_object)
    return prey_nearby
