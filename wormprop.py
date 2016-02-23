# wormprop.py - CS556 Assignment 2 
#             - this program studies worm propagation in different
#               types of graphs
#
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 
import sys
import networkx as nx


erg_file = "random-erg.graph"
bag_file = "random-bag.graph"
wsg_file = "random-wsg.graph"
graph_files = [erg_file, bag_file, wsg_file]


def test_nx () :
    """ Tests existence and functionality of networkx lib. """

    print "Test networkx library..."

    g = nx.Graph()
    g.add_edge('A', 'B', weight=4)
    g.add_edge('B', 'D', weight=2)
    g.add_edge('A', 'C', weight=3)
    g.add_edge('C', 'D', weight=4)
    path = nx.shortest_path(g, 'A', 'D', weight='weight')

    # print path
    assert(path == ['A', 'B', 'D'])

    print 'Good test, continue...'

def load_graph_from_file (filename) :
    graph = nx.read_edgelist(filename, delimiter=",", data=False)
    return graph

def propagate_worm (graph):
    graph.nodes() 

def usage () :
    print "usage: " + sys.argv[0] + \
          "GRAPH_FILE PROBABILITY_OF_INFECTION INITIAL_INFECTED_NODE" + \
          "[PROBABILITY_OF_CURE INITIAL_CURED_NODE]"

if __name__ == "__main__" :
	
    if (len(sys.argv) not in [4, 6]) :
        usage()
        exit()
    else:
        filename = sys.argv[1]
        prob_infect = float(sys.argv[2])
        init_node_attack = sys.argv[3]
        if (len(sys.argv) == 6) :
            prob_cure = float(sys.argv[4])
            init_node_defense = sys.argv[5]

	print "Assignment 2: Worm Propagation..."
	
	test_nx()
	
	print 'All tests passed!'

	print 'Loading network graph...'

    network = load_graph_from_file(filename)

    # check that init_node is actually a node in the network
    if (init_node_attack in network.nodes()) :
        # print "init_node is in the network! Yay!"
        pass
    else :
        print "init_node is not in the network! This is not going to work out."    
        exit()

    if (prob_infect > 0 and prob_infect < 1.0) :
        # print "probability of infection is within limits"
        pass
    else :
        print "probability of infection is out of limits"
        print prob_infect
        exit()
