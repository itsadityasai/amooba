import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

import sys
import os

# Add the @amooba directory to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '@amooba')))

# Now you can import
from GLOBALS import *


def create_plane_of_existence() -> None:
    for x in range(MIN_X, MAX_X+1, 1):
        for y in range(MIN_Y, MAX_Y+1, 1):
            print((x, y))
            db.env.insert_one({"point": [x, y], "object": None})

create_plane_of_existence()
