# wormprop.py - CS556 Assignment 2 
#             - this program studies worm propagation in different
#               types of graphs
#
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 
import sys, time, random
import networkx as nx


erg_file = "random-erg.graph"
bag_file = "random-bag.graph"
wsg_file = "random-wsg.graph"
graph_files = [erg_file, bag_file, wsg_file]

step = 0

class Network :

    def __init__ (self, init_graph, prob_infect, \
                  init_node_infected, prob_cure=0, init_node_healed=None) :
        self.graph = init_graph
        self.healthy = self.graph.nodes()[:]
        self.prob_infect = prob_infect 
        self.infected = [init_node_infected]
        for node in self.infected :
            self.healthy.remove(node)

        if (prob_cure > 0) :
            self.prob_cure = prob_cure
        if (init_node_healed != None) :
            self.safe = [init_node_healed]
    

    def status (self) :
        # print self.graph
        # print self.graph.nodes()
        print "Healthy: " + str(self.healthy)
        print "Infected: " + str(self.infected)
        print "Num healthy: " + str(self.get_num_healthy())
        print "Num infected: " + str(self.get_num_infected())

    def get_num_infected (self) :
        return len(self.infected)

    def get_num_healthy (self) :
        return len(self.healthy)

    def all_nodes_infected (self) :
        all_infected = True

        for node in self.graph.nodes() :
            if not self.is_infected(node) :
                all_infected = False

        return all_infected

    def is_infected (self, node) :
        return node in self.infected

    def all_nodes_healthy (self) :
        all_healthy = True

        for node in graph.nodes() :
            if not self.is_healthy(node) :
                all_healthy = False

        return all_healthy

    def is_healthy (self, node) :
        return node in self.healthy 

    def infect (self, node) :
        self.healthy.remove(node)
        self.infected.append(node)

    def infect_success (self) :
        return (random.random() < self.prob_infect) 

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

def complete (network) :
    is_complete = False

    if network.all_nodes_infected() :
        is_complete = True
    elif network.all_nodes_healthy() :
        is_complete = True
    else :
        is_complete = False

    return is_complete




def propagate_worm (network):
    global step 

    print ""
    print "Propagating, step " + str(step)
    network.status()
    
    # print "Nodes w/ self loops: "
    # print network.graph.nodes_with_selfloops()

    # for node in network.graph.nodes() :
         # print node + ": " + str(network.graph.neighbors(node))

    infect_candidates = []
    for worm in network.infected :
         # print "This in infected: " + worm
         infect_candidates.extend([nb for nb in network.graph.neighbors(worm) \
                                        if nb not in network.infected \
                                           and nb not in infect_candidates])

    infect_candidates = list(set(infect_candidates))

    print "To maybe infect this round: " + str(infect_candidates)
    
    infect_definite = [node for node in infect_candidates if network.infect_success()]

    for item in infect_definite :
         # print network.infected
         # print network.healthy
         network.infect(item)


    step += 1
    # time.sleep(1)

    num_infected = len(infect_definite)
    return num_infected

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
        init_node_attack = unicode(sys.argv[3])
        if (len(sys.argv) == 6) :
            prob_cure = float(sys.argv[4])
            init_node_defense = sys.argv[5]

	print "Assignment 2: Worm Propagation..."
	
	test_nx()
	
	print 'All tests passed!'

	print 'Loading network graph...'

    graph = load_graph_from_file(filename)

    # check that init_node is actually a node in the network
    if (init_node_attack in graph.nodes()) :
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


    # everything checks out, actually get started
    network = Network(graph, prob_infect, init_node_attack)


    while (not complete(network)) :
        num_infected = propagate_worm(network)
        print "Infected this round: " + str(num_infected)

    print ""
    print "END STATE: "
    network.status()
    print "Finally complete!" + " Rounds: " + str(step)
