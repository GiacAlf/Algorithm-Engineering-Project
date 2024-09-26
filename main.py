"""
the following algorith performs the computing of edge connectivity using 4 different sub-algorithms:
1 - Expander Decomposition
2 - Trimming
3 - Shaving
4 - ...
"""

import networkit as nk
import networkx as nx
from Graphs.graph_loader import GraphLoader
from sub_algorithms.expander_decomposition import ExpanderDecomposition
from sub_algorithms.trim import trim
from sub_algorithms.shave import shave
from sub_algorithms.contract_graph import contract_graph
from sub_algorithms.edge_connectivity import edge_connectivity


if __name__ == '__main__':
    # loads the graph
    file_path = 'Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Step 1: Expander decomposition
    phi = 40  # parameter φ
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # Trim and Shave steps
    trimmed_partitions = [trim(graph, set(partition.getMembers(subset))) for subset in partition.getSubsetIds()]
    shaved_partitions = [shave(graph, t) for t in trimmed_partitions]

    # Step 2: Contract the graph G'
    contracted_graph = contract_graph(graph, partition)

    # Step 3: Compute edge connectivity using Gabow's algorithm
    delta = min(graph.degree(u) for u in graph.iterNodes())
    lambda_prime = edge_connectivity(contracted_graph)
    result = min(lambda_prime, delta)

    print(f"Min{lambda_prime, delta}: {result}")
