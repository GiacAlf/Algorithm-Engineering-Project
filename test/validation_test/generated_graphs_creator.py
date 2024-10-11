"""
This script is used to generate a fixed number of simple graphs using
create_connected_simple_random_graph_with_weights function with fixed number of nodes and
random number of edges, saving them in CSV files in test graphs/generated_graphs.
"""

import os
import pandas as pd
from graphs.nx_simple_connected_graph_generator import create_connected_simple_random_graph_with_weights


def generate_and_save_graphs(nodes_list, output_dir):

    # cretes the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    for num_nodes in nodes_list:
        print(f"Generating graph with {num_nodes} nodes...")
        # graph generation
        graph = create_connected_simple_random_graph_with_weights(num_nodes, num_edges=None, fixed_weight=1)

        # graph conversion to dataframe
        edges = [(u, v, data['weight']) for u, v, data in graph.edges(data=True)]
        df = pd.DataFrame(edges)

        # save the graph to a CSV file
        output_file = os.path.join(output_dir, f"{num_nodes}_nodes.csv")
        df.to_csv(output_file, index=False, header=False)
        print(f"Saved graph with {num_nodes} nodes to {output_file}")


if __name__ == '__main__':

    """ GRAPHS CREATION """

    # fixed parameters
    num_graphs = 20  # total number of graphs to generate
    start_nodes = 10  # starting number of nodes
    step = 10  # increment of number of nodes

    max_nodes = start_nodes + (num_graphs-1) * step
    nodes_list = [i for i in range(start_nodes, max_nodes, step)]  # list of nodes
    print(nodes_list)   # to see the list

    output_dir = 'test_graphs/generated_graphs'  # output directory

    generate_and_save_graphs(nodes_list, output_dir)    # generates and saves the graphs
