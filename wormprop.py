# wormprop.py - CS556 Assignment 2 
#             - this program studies worm propagation in different
#               types of graphs
#
# author: kbmulligan
#         brett.mulligan@gmail.com
#
#
# 

import matplotlib
matplotlib.use("Agg")

import sys, time, random
import networkx as nx
import matplotlib.pyplot as plt

step = 0

class Network :

    def __init__ (self, init_graph, prob_infect, \
                  init_node_infected, prob_cure=0, init_node_healed=None) :
        self.graph = init_graph
        self.healthy = self.graph.nodes()[:]
        self.prob_infect = prob_infect 
        self.infected = [init_node_infected]
        self.prob_cure = 0
        self.cured = []

        for node in self.infected :
            self.healthy.remove(node)

        if (prob_cure > 0) :
            self.prob_cure = prob_cure
        if (init_node_healed != None) :
            self.cured = [init_node_healed]
    

    def status (self) :
        # print self.graph
        # print self.graph.nodes()
        # print "Healthy: " + str(self.healthy)
        # print "Infected: " + str(self.infected)
        print "Num healthy: " + str(self.get_num_healthy())
        print "Num infected: " + str(self.get_num_infected())
        print "Num cured: " + str(self.get_num_cured())

    def get_num_infected (self) :
        return len(self.infected)

    def get_num_healthy (self) :
        return len(self.healthy)

    def get_num_cured (self) :
        return len(self.cured)

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

    def is_cured (self, node) :
        return node in self.cured 

    def infect (self, node) :
        self.healthy.remove(node)
        self.infected.append(node)

    def infect_success (self) :
        return (random.random() < self.prob_infect) 

    def cure (self, node) :
        self.cured.append(node)

        # if not healthy, then make healthy
        if node not in self.healthy :
            self.healthy.append(node)

        # if infected, then stop it
        if node in self.infected :
            self.infected.remove(node)

    def cure_success (self) :
        return (random.random() < self.prob_cure) 


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


def propagate (network, stats=None) :
    global step 

    print ""
    print "Propagating, step " + str(step)
    network.status()


    # record stats here
    if (stats != None) :
        stats['infected'].append(network.get_num_infected()) 
        stats['healthy'].append(network.get_num_healthy()) 
        stats['cured'].append(network.get_num_cured()) 

    # do propagation steps here
    propagate_worm(network)
    propagate_cure(network)

    step += 1


def propagate_worm (network):

    # print "Nodes w/ self loops: "
    # print network.graph.nodes_with_selfloops()

    # for node in network.graph.nodes() :
         # print node + ": " + str(network.graph.neighbors(node))

    infect_candidates = []
    for worm in network.infected :
         # print "This in infected: " + worm
         infect_candidates.extend([nb for nb in network.graph.neighbors(worm) \
                                        if nb not in network.infected \
                                           and nb not in infect_candidates
                                           and nb not in network.cured])

    # uniqify
    infect_candidates = list(set(infect_candidates))

    # print "To maybe infect this round: " + str(infect_candidates)
    
    infect_definite = [x for x in infect_candidates if network.infect_success()]

    for item in infect_definite :
         # print network.infected
         # print network.healthy
         network.infect(item)

    num_infected = len(infect_definite)
    return num_infected

def propagate_cure (network) :
     
    cure_candidates = []
    for n_cured in network.cured :
         cure_candidates.extend([nb for nb in network.graph.neighbors(n_cured) \
                                        if nb not in network.cured \
                                           and nb not in cure_candidates])

    # uniqify
    cure_candidates = list(set(cure_candidates))

    cure_definite = [x for x in cure_candidates if network.cure_success()]

    for item in cure_definite :
         # print network.infected
         # print network.healthy
         network.cure(item)

    num_cured = len(cure_definite) 
    return num_cured

def save_figures (stats) :
    
    for key in stats.keys() :
        plt.clf() 
        plt.plot(stats[key]) 
        plt.savefig('results-' + filename + '-' + key + '.png')

def write_results (items) :
    with open("results.stats", "a") as results_file:

        for item in items:
            results_file.write(str(item) + " ")
        results_file.write("\n")


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
        prob_attack = float(sys.argv[2])
        init_node_attack = unicode(sys.argv[3])
        prob_defend = 0
        init_node_defend = None
        if (len(sys.argv) == 6) :
            prob_defend = float(sys.argv[4])
            init_node_defend = sys.argv[5]

    if (prob_attack > 0 and prob_attack < 1.0) :
        # print "probability of infection is within limits"
        pass
    else :
        print "probability of infection is out of limits"
        print prob_attack
        exit()

	print "Assignment 2: Worm Propagation..."

    # test networkx lib
	test_nx()
	print 'All tests passed!'

	print 'Loading network graph...'
    graph = load_graph_from_file(filename)

    # check that init_nodes are actually a node in the network
    if ( init_node_attack in graph.nodes() and (init_node_defend == None or init_node_defend in graph.nodes()) ) :
        # print "init_node is in the network! Yay!"
        pass
    else :
        print "init_node is not in the network! This is not going to work out."    
        exit()

    # everything checks out, actually get started
    network = Network(graph, prob_attack, init_node_attack, prob_defend, init_node_defend)
    stats = { 'healthy': [], 'infected': [], 'cured': [] }
    
    while (not complete(network)) :
        propagate(network, stats)

    # end caps for stats
    stats['infected'].append(network.get_num_infected()) 
    stats['healthy'].append(network.get_num_healthy()) 
    stats['cured'].append(network.get_num_cured()) 

    print ""
    print "END STATE: "
    network.status()
    print "Finally complete!" + " Rounds: " + str(step)

    for key in stats.keys() :
        print key, stats[key], len(stats[key])

    save_figures(stats)
    write_results([step, filename])
