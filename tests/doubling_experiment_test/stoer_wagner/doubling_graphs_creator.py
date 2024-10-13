"""
This script is used to generate a fixed number of simple graphs using
test/graphs_creation.generate_and_save_graphs function with a fixed number of nodes and a fixed or random
number of edges, saving them in CSV files in local tests_graphs/generated_graphs.
"""

from tests.graphs_creation import generate_and_save_graphs


if __name__ == '__main__':

    """ STOER-WAGNER DOUBLING EXPERIMENTS GRAPHS CREATION """

    """ In this main nodes and edges are fixed to generate the graphs, according to 
    O(m*n*log n) Stoer-Wagner time complexity. 
    All of this can be changes directly by user giving a node_list and and edge_list as parameters of 
    generate_and_save_graphs function."""

    # chosen graphs for testing
    nodes_list = []
    edges_list = []

    print(f"Nodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs'

    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
