"""This function is used to generate a fixed number of simple graphs, equals to node_list length, using
create_connected_simple_random_graph_with_weights function with fixed number of nodes and a fixed or random
 number of edges, saving them in CSV files in the given output_dir directory.
The randomness of the number of edges can be set either by giving edge_list = [] or len(edge_list) != len(node_list)
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

        if edge_list[i] is None:
            edge_list[i] = graph.number_of_edges()

        # save the graph to a CSV file
        output_file = os.path.join(output_dir, f"{nodes_list[i]}_nodes_{edge_list[i]}_edges.csv")
        df.to_csv(output_file, index=False, header=False)

        print(f"Saved graph with {nodes_list[i]} and {edge_list[i]} nodes to {output_file}")
