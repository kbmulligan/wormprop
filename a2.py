# a2.py - CS556 Assignment 2 - this program studies worm propagation
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 

import networkx as nx


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







if __name__ == "__main__" :
	
	print "Assignment 2: Worm Propagation..."
	
	test_nx()
	
	print 'All tests passed!'

