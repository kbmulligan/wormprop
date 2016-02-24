# wormprop
Studies worm propagation in networks

# Requires
networkx python library
 - pip install networkx

matplotlib python library
 - sudo apt-get install python-matplotlib (Debian-based)

# Usage
wormprop.py GRAPH_FILE PROBABILITY_OF_INFECTION INITIAL_INFECTED_NODE[PROBABILITY_OF_CURE INITIAL_CURED_NODE]

# Example
graph-create.py
worm-prop.py random-erg-1000.graph 0.3 0 0.5 999 
