# excecutes amooba.py for each amooba

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from sys import argv
from os import system
from subprocess import Popen

import os
import shutil

def reset_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)     # Deletes even non-empty directories
    os.makedirs(path)           # Recreates it

reset_directory("logs")


if argv[1] == '--all':
    amoobae = db.systems.find()
    for amooba in amoobae:
        Popen(f"python amooba.py {amooba['_id']}", shell=True)

if argv[1] == '--one':
    to_start = argv[2]
    system(f"python amooba.py {to_start}")
