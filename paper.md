---
title: "Amooba: A Distributed Artificial Life Simulation of Competing Digital Organisms"
tags:
  - artificial life
  - multi-agent systems
  - simulation
  - distributed systems
  - emergent behavior
  - python
authors:
  - name: Aditya Sai Shrinivas
    orcid: 0009-0001-0620-1925
    affiliation: 1
affiliations:
  - name: Independent Researcher
    index: 1
date: 17 July 2025
bibliography: paper.bib
---

# Summary

**Amooba** is a distributed artificial life simulation exploring emergent behavior in multi-agent systems. Each agent, or _amooba_, represents a simple digital organism capable of autonomous decision-making based on survival instincts: moving, hunting, feeding, and reproducing. These agents operate independently as separate processes, sharing state and interacting via a central MongoDB database.

The simulation models key aspects of biological systems, including energy-based survival, non-cannibalistic behavior toward kin, and population dynamics driven by natural selection. While simple in design, the system exhibits complex emergent behavior over time, making it an educational tool and proof-of-concept for scalable artificial life experiments.

Originally developed in 2021 as a learning project, Amooba is now released publicly as a research artifact. The code is modular and extensible, making it suitable for experimentation in artificial life, swarm behavior, and distributed agent-based modeling.

# Statement of Need

Simulations of artificial life often involve centralized architectures or simplified interactions. Amooba instead uses a fully distributed process-per-agent model, offering a more realistic concurrency framework that highlights performance trade-offs and emergent population dynamics in high-agent environments.

This project is useful for:

- Students learning about distributed systems and multi-agent simulations
- Researchers exploring emergent phenomena in digital ecosystems
- Developers prototyping artificial life or agent-based evolutionary systems

**It emphasizes modular architecture and extensibility, enabling users to introduce terrain, genetic traits, adaptive behavior, or event-driven communication with minimal refactoring.**

# Functionality

- Each _amooba_ is an independent Python process representing an autonomous agent.
- MongoDB is used as shared memory for real-time environment and organism state.
- Organisms expend and replenish energy by moving and feeding.
- High-energy organisms reproduce, while low-energy ones die.
- Agents avoid cannibalism of immediate relatives, introducing kin-based behavioral rules.
- The simulation supports real-time visualization of population and energy dynamics.

# Implementation and Architecture

- Python 3.x powers the core simulation logic.
- MongoDB provides persistent, concurrent access to shared state.
- Data analysis is supported via `pandas` and `matplotlib`.
- The simulation is launched and managed via terminal scripts (`start.py`, `createAmoobae.py`, etc.).
- Configuration is centralized in `GLOBALS.py` for easy customization.

Each agent performs proximity detection, movement, feeding, and reproduction checks in a loop, writing updates to the database. This design results in concurrent behavior patterns and population-level phenomena, such as boom-bust cycles and local resource competition.

# Reuse Potential

The codebase can be extended in several directions:

- **Custom behaviors**: Add learning, memory, or more complex AI.
- **Environmental enhancements**: Introduce obstacles, terrain, or food sources.
- **Evolutionary simulations**: Encode heritable traits and track fitness over generations.
- **Performance optimization**: Replace process-per-agent model with asynchronous scheduling or actor-based frameworks.

Educationally, Amooba serves as a bridge between theory and practice in distributed systems, ecology modeling, and agent-based simulations.

# Acknowledgements

This work was developed independently as part of a personal research initiative in artificial life and distributed systems.
