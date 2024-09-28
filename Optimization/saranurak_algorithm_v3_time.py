"""
SARANURAK ALGORITHM

The following algorithm performs edge connectivity on simple graphs.
The computation is performed using 4 different sub-algorithms applied in the following order:
1 - Expander Decomposition: Expander(G, φ) implemented in expander_decomposition_v3.py
2 - Trimming: Trim(G, S) implemented in trim_v3.py
3 - Shaving: Shave(G, S) implemented in shave_v3.py
4 - Gabow's edge connectivity: edge_connectivity(G) implemented in edge_connectivity_v3.py
"""

import time
from Graphs.graph_loader_v3 import GraphLoader
from Sub_algorithms.expander_decomposition_v3 import ExpanderDecomposition
from Sub_algorithms.trim_v3 import trim
from Sub_algorithms.shave_v3 import shave
from Sub_algorithms.contract_graph_v3 import contract_graph
from Sub_algorithms.edge_connectivity_v3 import edge_connectivity


def saranurak_algorithm(graph):
    """
    Executes the Saranurak algorithm to compute the edge connectivity of the input graph.

    :param graph: Input graph (assumed to be loaded as a NetworKit graph)
    :return: The edge connectivity of the graph
    """
    # Assert that the graph is not empty
    if graph.numberOfNodes() == 0:
        raise ValueError("The graph must have at least one node")

    # Step 1: Expander decomposition
    phi = 40  # parameter φ fixed in the Saranurak paper
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    if partition.numberOfSubsets() == 0:
        raise RuntimeError("Partitioning failed: no subsets found")

    # Step 2: Trim each subset of the partition
    trimmed_partitions = []
    for subset in partition.getSubsetIds():
        members = set(partition.getMembers(subset))
        trimmed_set = trim(graph, members)

        if len(trimmed_set) > len(members):
            raise RuntimeError("Trimmed set should not be larger than the original subset")

        trimmed_partitions.append(trimmed_set)

    # Step 3: Shave the trimmed partitions
    shaved_partitions = []
    for t in trimmed_partitions:
        shaved_set = shave(graph, t)

        if not set(shaved_set).issubset(t):
            raise RuntimeError("Shaved set should be a subset of the trimmed set")

        shaved_partitions.append(shaved_set)

    # Extra Step: Contract the graph G' to feed into Gabow's algorithm
    contracted_graph = contract_graph(graph, partition)

    if contracted_graph.numberOfNodes() > graph.numberOfNodes():
        raise RuntimeError("Contracted graph cannot have more nodes than the original graph")

    # Step 4: Compute edge connectivity using Gabow's algorithm
    delta = min(graph.degree(u) for u in graph.iterNodes())  # Minimum degree in the original graph
    lambda_prime = edge_connectivity(contracted_graph)  # Edge connectivity in the contracted graph

    if lambda_prime < 0:
        raise ValueError("Edge connectivity must be non-negative")

    result = min(lambda_prime, delta)

    return result


if __name__ == '__main__':
    # Load the graph from a CSV file
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Start measuring time
    start_time = time.time()

    # Run the Saranurak algorithm and compute the edge connectivity
    edge_conn = saranurak_algorithm(graph)

    # End measuring time
    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Edge Connectivity: {edge_conn}")
    print(f"Time taken to complete the process: {elapsed_time:.4f} seconds")
