import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from sys import exit as die
from time import sleep

import pandas as pd
import matplotlib.pyplot as plt

print("Started")

second = 0
d = []

try:
    while True:
        x = db.systems.count_documents({})
        d.append([f'{second}', x])
        sleep(1)
        second += 1
except KeyboardInterrupt:
    df = pd.DataFrame(d)
    print(df)
    df.plot()
    plt.show()
    die()
