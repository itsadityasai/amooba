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
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
    
    # Population plot
    df = pd.DataFrame(d, columns=['Time', 'Population'])
    df['Time'] = df['Time'].astype(int)
    ax1.plot(df['Time'], df['Population'], 'b-', linewidth=2)
    ax1.set_title('Population Over Time')
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('Number of Organisms')
    ax1.grid(True, alpha=0.3)
    
    # Energy plot
    ef = pd.DataFrame(el, columns=['Total_Energy'])
    time_values = range(len(ef))
    ax2.plot(time_values, ef['Total_Energy'], 'r-', linewidth=2)
    ax2.set_title('Total Energy Over Time')
    ax2.set_xlabel('Time (seconds)')
    ax2.set_ylabel('Total Energy (excluding base 100)')
    ax2.grid(True, alpha=0.3)
    
    # Adjust layout to prevent overlap
    plt.tight_layout()
    plt.show()
    die()