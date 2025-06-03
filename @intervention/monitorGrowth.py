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
el = []

try:
    while True:

        x = db.systems.count_documents({})
        d.append([f'{second}', x])

        e = db.systems.aggregate([{"$group": {"_id": None, "sum_val": {"$sum":"$energy"}}}])
        for er in e:
            el.append(er['sum_val'] - 100)

        sleep(1)
        second += 1
except KeyboardInterrupt:
    df = pd.DataFrame(d)
    rar = df.plot()

    ef = pd.DataFrame(el)
    ef.plot(ax=rar)
    # plt.plot(df, ef)

    plt.show()
    die()
