# a2.py - CS556 Assignment 2
#       - this program creates graphs to study worm propagation
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 
import sys
import networkx as nx

nodes_nlt = 100
nodes_ngt = 10000

nodes = 1000

erg_file = "random-erg-"+str(nodes)+".graph"
bag_file = "random-bag-"+str(nodes)+".graph"
wsg_file = "random-wsg-"+str(nodes)+".graph"

def test_nx () :
    """ Tests existence and functionality of networkx lib. """

    print "Test networkx library..."

    g = nx.Graph()
    g.add_edge('A', 'B', weight=4)
    g.add_edge('B', 'D', weight=2)
    g.add_edge('A', 'C', weight=3)
    g.add_edge('C', 'D', weight=4)
    path = nx.shortest_path(g, 'A', 'D', weight='weight')

    print path

    print 'Good test, continue...'


def create_graphs (num_nodes=10, prob_edge=0.1, edges_for_new_nodes=5, 
                   k_nearest=5, prob_rewiring=0.05) :

    erg = nx.gnp_random_graph(num_nodes, prob_edge) 
    bag = nx.barabasi_albert_graph(num_nodes, edges_for_new_nodes)
    wsg = nx.watts_strogatz_graph(num_nodes, k_nearest, prob_rewiring)

    print erg
    print bag
    print wsg

    nx.write_edgelist(erg, erg_file, delimiter=",", data=False)
    nx.write_edgelist(bag, bag_file, delimiter=",", data=False)
    nx.write_edgelist(wsg, wsg_file, delimiter=",", data=False)

def usage () :
    print "Usage: " + sys.argv[0] + "<graph type> <filename>"


if __name__ == "__main__" :
	
    # if (len(sys.argv) != 3):
        # usage()

    print "Assignment 2: Graph creator..."
    test_nx()
    create_graphs(nodes)

    print 'All tests passed!'

