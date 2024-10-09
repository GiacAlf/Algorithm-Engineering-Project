import csv
import os
import networkx as nx

from Graphs.graph_loader import GraphLoader

# import pdb




if __name__ == '__main__':
    file_path = '../Graphs/generated_graphs/generated_graph_with_weights.csv'  # Path to your CSV file

    # pdb.set_trace()
    # Load the graph from the CSV file
    loader = GraphLoader(file_path)

    # Carica il grafo dal CSV con capacità predefinita di 1
    graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

    # Assert that the graph is not empty
    assert graph.number_of_nodes() > 0, "The graph must have at least one node"

    # Check for isolated nodes
    assert all(graph.degree(node) > 0 for node in graph.nodes()), "The graph contains isolated nodes"

    # Calculate edge connectivity using networkx
    edge_connectivity = nx.edge_connectivity(graph)

    print(f"NetworkX edge connectivity value is: {edge_connectivity}")
