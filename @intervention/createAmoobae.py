import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

def getLatestAmooba():
    rec = db.systems.find(sort=[("_id", -1)]).limit(1) # descending order sort
    return rec[0]['_id']

def createNewDefaultAmooba():

    amooba_to_create = int(getLatestAmooba() + 1)

    child = {

        "_id" : amooba_to_create,
        "energy" : 100,
        "parent" : "amooba0",

    }

    db.systems.insert_one(child)

    free_location = db.env.find_one({'object' : None})
    db.env.update_one(
        {

            'point': free_location['point']

        },
        {

            '$set': {
                'object': f'amooba{amooba_to_create}'
            }
        }
    )

for i in range(15):
    createNewDefaultAmooba() # organism 0 must exist previously

