
# NOTE:  amoobae can currently not run away

import pymongo
client = pymongo.MongoClient("localhost", 27017)
db = client.amooba

from GLOBALS import *


def __delete(_id) -> None:
    db.systems.remove({'_id': _id})
    db.env.update_one(
        {'object': f'amooba{_id}'},
        {'$set': {'object': None}}
    )

def eat(predator, prey) -> None: # only run on nearby amoobae (see plane.py) # does not check if needsToEat()

    from energy import getEnergy, increaseEnergy

    prey_energy = getEnergy(prey)
    passed_on_energy = (10/100) * prey_energy # 10% goes to the next trophic level irl

    increaseEnergy(predator, passed_on_energy) # no need to handle any exception as hunting will only take place if the predator is low on energy

    __delete(prey)

def hunt(predator) -> list: # doesn't check if needsEnergy()

    from movement import goto
    from plane import get_nearby_amoobae
    from random import randint
    from energy import needsEnergy
    from reproduce import getParent

    hunted = []

    stop_hunting = False
    for x in range(MIN_X-1, MAX_X+1, 1):
        for y in range(MIN_Y-1, MAX_Y+1, 1):
            arrived = goto(predator, [x, y])
            if arrived:
                nearby_prey = get_nearby_amoobae(predator)
                if len(nearby_prey) > 0:
                    to_eat = nearby_prey[randint(0, len(nearby_prey) - 1)]
                    if ( predator != getParent(int(to_eat['object'].replace('amooba', ''))) ) and (getParent(predator) != int(to_eat['object'].replace('amooba', ''))) and (getParent(predator) != getParent(int(to_eat['object'].replace('amooba', '')))): #don't eat your child ; don't eat your parent ; don't eat your sibling; 
                        eat(predator, int(to_eat['object'].replace('amooba', '')))
                        hunted.append(to_eat)
                    if needsEnergy(predator):
                        continue
                    else:
                        stop_hunting = True
                        break
        if stop_hunting:
            break

    return hunted
