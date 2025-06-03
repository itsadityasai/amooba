import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba


def create_plane_of_existence() -> None:
    for x in range(-500, +501, 1):
        for y in range(-500, +501, 1):
            print((x, y))
            db.env.insert_one({"point": [x, y], "object": None})

create_plane_of_existence()
