"""
SARANURAK ALGORITHM

The following algorithm performs edge connectivity on simple graphs.
The computation is performed using 4 different sub-algorithms applied in the following order:
1 - Expander Decomposition: Expander(G, φ) implemented in expander_decomposition_v3.py
2 - Trimming: Trim(G, S) implemented in trim_v3.py
3 - Shaving: Shave(G, S) implemented in shave_v3.py
4 - Gabow's edge connectivity: edge_connectivity(G) implemented in edge_connectivity_v3.py
"""

from Graphs.graph_loader import GraphLoader
from Sub_algorithms.expander_decomposition_v2 import ExpanderDecomposition
from Sub_algorithms.trim_v2 import trim
from Sub_algorithms.shave_v2 import shave
from Sub_algorithms.contract_graph_v2 import contract_graph
from Sub_algorithms.edge_connectivity_v2 import edge_connectivity

if __name__ == '__main__':
    # Load the graph from a CSV file
    file_path = 'Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Assert that the graph is not empty
    assert graph.numberOfNodes() > 0, "The graph must have at least one node"

    # Step 1: Expander decomposition
    phi = 40  # parameter φ fixed in the Saranurak paper
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # Assert that the partitioning has been successful
    assert partition.numberOfSubsets() > 0, "Partitioning failed: no subsets found"

    # Step 2: Trim each subset of the partition
    trimmed_partitions = []
    for subset in partition.getSubsetIds():
        members = set(partition.getMembers(subset))
        trimmed_set = trim(graph, members)

        # Assert that the trimmed set is not larger than the original subset
        assert len(trimmed_set) <= len(members), "Trimmed set should not be larger than the original subset"

        trimmed_partitions.append(trimmed_set)

    # Step 3: Shave the trimmed partitions
    shaved_partitions = []
    for t in trimmed_partitions:
        shaved_set = shave(graph, t)

        # Assert that the shaved set is a subset of the trimmed set
        assert set(shaved_set).issubset(t), "Shaved set should be a subset of the trimmed set"

        shaved_partitions.append(shaved_set)

    # Extra Step: Contract the graph G' to feed into Gabow's algorithm
    contracted_graph = contract_graph(graph, partition)

    # Assert that the contracted graph has fewer or the same number of nodes
    assert contracted_graph.numberOfNodes() <= graph.numberOfNodes(), ("Contracted graph cannot have more nodes than "
                                                                       "the original graph")

    # Step 4: Compute edge connectivity using Gabow's algorithm
    delta = min(graph.degree(u) for u in graph.iterNodes())  # Minimum degree in the original graph
    lambda_prime = edge_connectivity(contracted_graph)  # Edge connectivity in the contracted graph

    # Assert that lambda_prime is a non-negative value
    assert lambda_prime >= 0, "Edge connectivity must be non-negative"

    result = min(lambda_prime, delta)

    print(f"Min({lambda_prime}, {delta}): {result}")
