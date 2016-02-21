# a2.py - CS556 Assignment 2
#       - this program creates graphs to study worm propagation
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 
import sys
import networkx as nx


filename = ""


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




def usage () :
    print "Usage: " + sys.argv[0] + "<graph type> <filename>"


if __name__ == "__main__" :
	
    if (len(sys.argv) != 3):
        usage()
        exit()

    print "Assignment 2: Graph creator..."
    test_nx()
 
    print 'All tests passed!'

