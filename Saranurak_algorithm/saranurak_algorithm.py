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
# from Sub_algorithms.expander_decomposition import ExpanderDecomposition
from Sub_algorithms.expander_decomposition_v2 import ExpanderDecomposition
# from Sub_algorithms.trim import trim
from Sub_algorithms.trim_v2 import trim
# from Sub_algorithms.shave import shave
from Sub_algorithms.shave_v2 import shave
# from Sub_algorithms.contract_graph import contract_graph
from Sub_algorithms.contract_graph_v2 import contract_graph
# from Sub_algorithms.edge_connectivity import edge_connectivity
from Sub_algorithms.edge_connectivity_v2 import edge_connectivity


if __name__ == '__main__':
    # loads the graph
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Step 1: Expander decomposition
    phi = 40  # parameter φ fixed in Saranurak paper
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # Step 2: Trim
    trimmed_partitions = [trim(graph, set(partition.getMembers(subset))) for subset in partition.getSubsetIds()]

    # Step 3: Shave
    shaved_partitions = [shave(graph, t) for t in trimmed_partitions]

    # Extra Step: Contract the graph G' to feed into Gabow's algorithm
    contracted_graph = contract_graph(graph, partition)

    # Step 4: Computing edge connectivity using Gabow's algorithm
    delta = min(graph.degree(u) for u in graph.iterNodes())
    lambda_prime = edge_connectivity(contracted_graph)
    result = min(lambda_prime, delta)

    print(f"Min{lambda_prime, delta}: {result}")
