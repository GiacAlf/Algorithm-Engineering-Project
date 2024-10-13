"""
This script is used to generate a fixed number of simple graphs using
tests/graphs_creator.generate_and_save_graphs function with fixed number graph, fixed number of nodes and
random number of edges set as parameters, saving them in CSV files in local tests_graphs/generated_graphs.
"""

from tests.graphs_creation import generate_and_save_graphs

if __name__ == '__main__':

    """ GRAPHS CREATION """

    """ with the parameters below, it can be generated num_graphs graphs with num_nodes nodes each
     and the number of edges randomly selected or setted by the user.
     The step parameter sets the increment of the number of node from the previous one."""

    # fixed parameters, change this parameters if needed
    num_graphs = 20  # total number of graphs to generate
    start_nodes = 10  # starting number of nodes
    step = 10  # increment of number of nodes

    max_nodes = start_nodes + (num_graphs-1) * step

    nodes_list = [i for i in range(start_nodes, max_nodes, step)]

    # to see the list of nodes
    print(nodes_list)

    # edge list is empty so the number of edges is chosen randomly but in can be set with user input, but it must
    # be of the same number of elements of nodes_list, otherwise the edges will be still selected randomly
    edge_list = []

    # output directory
    output_dir = 'test_graphs/generated_graphs'

    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edge_list, output_dir)
