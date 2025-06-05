# Amooba — Ecosystem Simulation

A multi-agent artificial life simulation where simple organisms (amoobae) compete for survival in a 2D environment. Each amooba is an independent process that can move, hunt, feed, and reproduce based on energy levels and survival instincts.

## About

This project simulates a population of digital organisms called "amoobae" that exhibit emergent behaviors through simple rules:

- **Energy Management**: Organisms must maintain energy levels by hunting others
- **Spatial Movement**: Amoobae navigate a 2D grid environment
- **Reproduction**: High-energy organisms can create offspring
- **Natural Selection**: Energy-depleted organisms die, creating evolutionary pressure
- **Family Relations**: Organisms won't eat immediate family members (parents, children, siblings)

Each amooba runs as a separate Python process, making decisions independently based on its current state and environment. The simulation tracks population dynamics, energy distribution, and generational changes over time.

## Software Used

- **Python 3.x** - Core simulation logic
- **MongoDB** - Database for organism states and environment
- **pymongo** - MongoDB Python driver
- **pandas** - Data analysis and monitoring
- **matplotlib** - Population growth visualization
- **colorama** - Console output formatting

## Directory Structure

```
amooba/
├── @amooba/                  # All these modules together make up a functioning amooba
   ├── amooba.py              # Main organism behavior loop
   ├── start.py               # Process spawning and management
   ├── console.py             # Colored console logging
   ├── GLOBALS.py             # Configuration constants
   ├── energy.py              # Energy management system
   ├── feed.py                # Hunting and eating mechanics
   ├── movement.py            # Spatial navigation
   ├── plane.py               # 2D environment and proximity detection
   ├── reproduce.py           # Reproduction and offspring creation
   └── logs/                  # Movement logs for each organism
├── @intervention/            # Manual setup or observation
   ├── createAmoobae.py       # Initial population setup
   ├── createEnvironment.py   # Environment grid initialization
   └── monitorGrowth.py       # Real-time population monitoring
├── db/
   ├── start_db.bat           # MongoDB startup script
   ├── restoreDB.bat          # Database restoration command
   └── db_backup/             # Database backups are stored here
├── graphs/                   # Graphs plotted by me during test runs
```

## Project History

This simulation was originally developed in 2021 as an exploration into artificial life systems and multi-agent behavior. After completing the core functionality and achieving the intended emergent behaviors, the project was set aside as I moved on to other endeavors.

In 2025, I've decided to make this work publicly available, recognizing both its educational value and the interesting approaches it demonstrates. Looking back with several years of additional experience, I can identify numerous areas where the architecture and implementation could be optimized—from the process-per-organism model to database interaction patterns. However, this project represents an important milestone in understanding distributed systems, artificial life principles, and emergent behavior modeling.

Rather than rewriting it entirely, I'm sharing the original implementation as both a functional simulation and a snapshot of problem-solving approaches from that time. The code successfully demonstrates complex multi-agent interactions and serves as an excellent foundation for others to build upon, optimize, or reimagine entirely.

## How to Run

### Prerequisites

1. Install MongoDB and ensure it's accessible locally
2. Install required Python packages:
   ```bash
   pip install pymongo pandas matplotlib colorama
   ```

### Setup

1. **Start MongoDB Database**:

   ```bash
   # Windows
   start_db.bat

   # Manual start
   mongod.exe --dbpath ./data/ --maxConns 10000000
   ```

2. Restore the database from backup
   ```bash
   restoreDB.bat
   ```

OR manually initialize

2. **Initialize Environment**:

   ```bash
   python createEnvironment.py
   ```

3. **Create Initial Population**:
   ```bash
   python createAmoobae.py
   ```

### Running the Simulation

1. **Start All Organisms**:

   ```bash
   python start.py --all
   ```

2. **Monitor Population Growth** (optional, separate terminal):

   ```bash
   python monitorGrowth.py
   ```

3. **Start Individual Organism** (for testing):
   ```bash
   python start.py --one <organism_id>
   ```

### Configuration

Easily modify simulation parameters in `GLOBALS.py`:

```python
# Energy thresholds
NEW_ENERGY_VAL = 60        # Energy threshold for hunting vs reproducing
MIN_ENERGY_VAL = 1         # Death threshold
MAX_ENERGY_VAL = 100       # Maximum energy capacity

# Environment size
MIN_X = -500               # Grid boundaries
MAX_X = 500
MIN_Y = -500
MAX_Y = 500

# Movement costs
ENERGY_MOVEMENT_DROP = 100 # Energy cost per distance unit

# Proximity detection
NEARBY_X = 5               # Detection radius
NEARBY_Y = 5

# Reproduction
CHILD_SPAWN_ENERGY = 100   # Offspring starting energy
PARENT_ENERGY_DROP = 50    # Energy cost to parent
```

## System Architecture

The simulation uses a distributed process model where:

- Each amooba runs as an independent Python process
- MongoDB serves as shared memory for organism states and environment
- Processes communicate indirectly through database reads/writes
- Real-time monitoring tracks emergent population dynamics

This architecture allows for true concurrent behavior but comes with performance trade-offs.

## Extensibility

The codebase is designed for easy modification and extension:

- **Adding New Behaviors**: Extend the main loop in `amooba.py`
- **New Object Types**: The environment system in `plane.py` accommodates any object type
- **Custom Energy Sources**: Modify `feed.py` to add non-organism food sources
- **Environmental Hazards**: Add obstacles or dangerous zones in the environment
- **Genetic Traits**: Extend organism properties beyond just energy levels
- **Different Movement Patterns**: Replace teleportation with realistic movement in `movement.py`

## Images

The simulation generates real-time population graphs through `monitorGrowth.py`:

- Population count over time
- Total energy distribution
- Growth rate visualization

_Run the monitor script during simulation to see live population dynamics_

## Known Issues

### Performance Limitations

- **System Heavy**: Creates one Python process per organism, leading to high CPU and memory usage
- **Socket Connections**: Limited by MongoDB connection pool (currently set to 10M max connections)
- **Inefficient Architecture**: Built during early learning phase, prioritizing functionality over optimization
- **Memory Leaks**: Long-running simulations may accumulate memory usage

### Simulation Limitations

- **Single Spawn Point**: All new organisms spawn at the same location, creating unrealistic clustering
- **Teleportation Movement**: Organisms "jump" instantly to new locations rather than gradual movement
- **No Terrain**: Environment is completely uniform with no obstacles or varied food sources
- **Simple AI**: Organisms use basic algorithms without learning or adaptation
- **Race Conditions**: Concurrent database access may cause occasional inconsistencies

### Recommendations for Improvement

1. **Process Pooling**: Use a worker pool instead of spawning unlimited processes
2. **Realistic Movement**: Implement gradual movement with pathfinding
3. **Spatial Distribution**: Random spawn locations for new organisms
4. **Caching**: Reduce database calls with local state caching
5. **Event-Driven**: Replace polling with event-based updates

## Contributing

This project serves as a foundation for artificial life experiments. The clean, modular code structure makes it easy to:

- Add new organism behaviors
- Implement different survival strategies
- Experiment with evolutionary parameters
- Extend the environment complexity

Feel free to fork, modify, and improve upon this simulation!

## License

## This code is open source and licensed under the BSD-3-Clause License.

_Note: This simulation can quickly consume system resources. Monitor CPU and memory usage, especially with large populations (>100 organisms)._
