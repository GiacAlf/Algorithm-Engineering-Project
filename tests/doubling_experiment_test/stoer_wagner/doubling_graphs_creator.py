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

    # TEST 1: check if O(m) part of the Stoer-Wagner time complexity is really linear, keeping n constant.
    # expectation is that doubling m each time also the time is doubled (so we expect a line in a graph representation)

    # test 1.1: fixed number of nodes = 64, doubled number of edges
    nodes_list = [64, 64, 64, 64, 64]
    edges_list = [64, 128, 256, 512, 1024]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.2: fixed number of nodes = 128, doubled number of edges
    nodes_list = [128, 128, 128, 128, 128, 128]
    edges_list = [128, 256, 512, 1024, 2048, 4096]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 1.3: fixed number of nodes = 256, doubled number of edges
    nodes_list = [256, 256, 256, 256, 256, 256, 256]
    edges_list = [256, 512, 1024, 2048, 4096, 8192, 16384]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_1_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # TEST 2: check if O(n*log(n)) part is really log-linear keeping m constant.
    # expectation is that doubling n each time also the time is more than doubled (so we expect a log-line)

    # test 2.1: fixed number of edges = 1024, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [1024, 1024, 1024, 1024, 1024]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_1'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.2: fixed number of edges = 1500, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [1500, 1500, 1500, 1500, 1500]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_2'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)

    # test 2.3: fixed number of edges = 2000, doubled number of nodes
    nodes_list = [64, 128, 256, 512, 1024]
    edges_list = [2000, 2000, 2000, 2000, 2000]

    print(f"\nNodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # output directory
    output_dir = 'test_graphs/generated_graphs_test_2_3'
    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
