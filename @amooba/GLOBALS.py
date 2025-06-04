
# amooba.py
LOGFILE_NAME = "movement"

# energy.py
NEW_ENERGY_VAL = 60 # organisms with energy below this are marked as "needing energy" (they must hunt, can't reproduce)
MIN_ENERGY_VAL = 1
MAX_ENERGY_VAL = 100

# feed.py
MIN_X = -500
MAX_X = 500
MIN_Y = -500
MAX_Y = 500

# movement.py
ENERGY_MOVEMENT_DROP = 100 # energy -= DISTANCE/ENERGY_MOVEMENT_DROP

# plane.py
NEARBY_X = 5
NEARBY_Y = 5

# reproduce.py
CHILD_SPAWN_ENERGY = 100
PARENT_ENERGY_DROP = 50