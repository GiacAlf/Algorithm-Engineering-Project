import csv
import os
import networkx as nx
# import pdb


# This function loads a graph from a CSV file
def load_graph_from_csv(file_path):
    graph = nx.Graph()
    with open(file_path, mode="r") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header
        for row in reader:
            source, target = map(int, row)
            graph.add_edge(source, target)
    return graph


if __name__ == '__main__':
    file_path = '../Graphs/generated_graphs/generated_graph.csv'  # Path to your CSV file

    # pdb.set_trace()
    # Load the graph from the CSV file
    graph = load_graph_from_csv(file_path)

    # Assert that the graph is not empty
    assert graph.number_of_nodes() > 0, "The graph must have at least one node"

    # Check for isolated nodes
    assert all(graph.degree(node) > 0 for node in graph.nodes()), "The graph contains isolated nodes"

    # Calculate edge connectivity using networkx
    edge_connectivity = nx.edge_connectivity(graph)

    print(f"Edge connectivity of the loaded graph: {edge_connectivity}")
