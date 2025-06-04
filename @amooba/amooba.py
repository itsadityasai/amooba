# exececuted by start.py for each amooba

from sys import argv
import console
from sys import exit as die

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

_id = int(argv[1])

import energy, feed, movement, plane, reproduce
from datetime import datetime
from random import randint
from GLOBALS import *

# NOTE: not really accurate because there is no lock

movement.logfile = open(f"logs/{LOGFILE_NAME}.log", 'a')

try:

    while True:

        if energy.needsEnergy(_id):
            try:
                console.log(f"[{str(datetime.now())}] amooba{_id} needs energy, hunting")
                console.warn(f"[{str(datetime.now())}] organism {_id} just had some food : {feed.hunt(_id)}")
            except energy.InvalidEnergyErr:
                console.error(f"[{str(datetime.now())}] amooba{_id} just died due to loss of energy")
                feed.__delete(_id)
                die()

        else:
            if reproduce.canReproduce(_id):
                # console.log(f"[{str(datetime.now())}] amooba{_id} has energy, reproducing")
                console.warn(f"[{str(datetime.now())}] organsim {_id} just had a baby! : {reproduce.reproduce(_id)}")

except Exception as e:

    console.error(f"[{str(datetime.now())}] organism {_id} : Exception : {e}")
    db.systems.delete_one({'_id' : _id})
    die()
