"""
This script is used to generate a fixed number of simple graphs using
test/graphs_creation.generate_and_save_graphs function with a fixed number of nodes and  a fixed or random
number of edges, saving them in CSV files in local tests_graphs/generated_graphs.
"""

from tests.graphs_creation import generate_and_save_graphs


# create the nodes list for doubling experiment
def create_nodes_list_doubling_experiment(start_node, num_graph):
    nodes_list = [start_node]
    for _ in range(1, num_graph):
        next_node = nodes_list[-1] * 2
        nodes_list.append(next_node)
    return nodes_list


# create the edges list for doubling experiment
def create_edges_list_doubling_experiment(start_edge, num_graph):
    edges_list = [start_edge]
    for _ in range(1, num_graph):
        next_edge = edges_list[-1] * 2
        edges_list.append(next_edge)
    return edges_list


if __name__ == '__main__':

    """ FORD FULKERSON DOUBLING EXPERIMENTS GRAPHS CREATION """

    """ In this main some fixed parameters are chosen to generate the graphs with fixed number of nodes and 
    fixed number of edges, doubling each time from the previous one.
     All of this can be changes directly by user giving a node_list and an edge_list as parameters of 
     generate_and_save_graphs function."""

    # fixed parameters, chosen this way because of Ford-Fulkerson O(n^7) time complexity
    start_node = 4
    start_edge = 6
    num_graph = 9

    # create a list of nodes, doubling each time from start_node
    nodes_list = create_nodes_list_doubling_experiment(start_node, num_graph)

    # create a list of edges, doubling each time from start_edge
    edges_list = create_edges_list_doubling_experiment(start_edge, num_graph)

    print(f"Nodes list: {nodes_list}")
    print(f"Edges list: {edges_list}")

    # uncomment the following lines to generate the graphs with random edges
    # edges_list =[]

    # output directory
    output_dir = 'test_graphs/generated_graphs'

    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
