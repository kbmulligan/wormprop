# wormprop
Studies worm propagation in networks

# Requires
networkx python library
 - pip install networkx

matplotlib python library
 - sudo apt-get install python-matplotlib (Debian-based)

# Usage
`wormprop.py FILE PROB_OF_INFECTION INIT_INFECTED_NODE [PROB_OF_CURE INIT_CURED_NODE]`

# Example
    graph-create.py
    worm-prop.py random-erg-1000.graph 0.3 0 0.5 999
