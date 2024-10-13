"""
This script is used to generate a fixed number of simple graphs using
create_connected_simple_random_graph_with_weights function with fixed number of nodes and
random number of edges, saving them in CSV files in tests graphs/generated_graphs.
"""

import os
import pandas as pd
from graphs.nx_simple_connected_graph_generator import create_connected_simple_random_graph_with_weights


def generate_and_save_graphs(nodes_list, edge_list, output_dir):
    # cretes the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    # node_list nad edge_list must have the same length, otherwise edges will be selected randomly
    if len(nodes_list) != len(edge_list):
        edge_list = [None] * len(nodes_list)

    for i in range(len(nodes_list)):
        print(f"Generating graph with {nodes_list[i]} nodes and {edge_list[i]} edges...")
        # graph generation
        graph = create_connected_simple_random_graph_with_weights(nodes_list[i], num_edges=edge_list[i],
                                                                      fixed_weight=1)

        # graph conversion to dataframe
        edges = [(u, v, data['weight']) for u, v, data in graph.edges(data=True)]
        df = pd.DataFrame(edges)

        # save the graph to a CSV file
        output_file = os.path.join(output_dir, f"{nodes_list[i]}_nodes_{edge_list[i]}_edges.csv")
        df.to_csv(output_file, index=False, header=False)
        print(f"Saved graph with {nodes_list[i]} and {edge_list[i]} nodes to {output_file}")


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

    """ GRAPHS CREATION """

    # fixed and wise parameters
    start_node = 4
    start_edge = 6
    num_graph = 9

    # create a list of nodes, doubling each time from start_node
    nodes_list = create_nodes_list_doubling_experiment(start_node, num_graph)

    # create a list of edges, doubling each time from start_edge
    edges_list = create_edges_list_doubling_experiment(start_edge, num_graph)

    print(nodes_list)
    print(edges_list)

    # uncomment the following lines to generate the graphs with random edges, not advisable for more than 8 nodes
    # edges_list =[None]

    # output directory
    output_dir = 'test_graphs/generated_graphs'

    # generates and saves the graphs
    generate_and_save_graphs(nodes_list, edges_list, output_dir)
