import networkit as nk
import networkx as nx
import random
from Graphs.graph_loader import GraphLoader
from sub_algorithms.expander_decomposition import ExpanderDecomposition
from sub_algorithms.trim import trim
from sub_algorithms.shave import shave
from sub_algorithms.contract_graph import contract_graph


def karger_edge_connectivity(graph):
    # Create a new NetworkX graph from the Networkit graph
    g = nx.Graph()

    # Add nodes and edges from the Networkit graph
    for node in graph.iterNodes():
        g.add_node(node)
    for edge in graph.iterEdges():
        g.add_edge(edge[0], edge[1])

    n = g.number_of_nodes()

    # Continue until only two nodes remain
    while g.number_of_nodes() > 2:
        # Randomly select an edge
        u, v = random.choice(list(g.edges()))

        # Merge the two vertices
        g = nx.contracted_nodes(g, u, v, self_loops=False)

    # Return the number of edges in the contracted graph (this is the minimum cut)
    return g.number_of_edges()


if __name__ == '__main__':
    # Load the graph
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

    # Step 3: Compute edge connectivity using Karger's algorithm
    karger_result = karger_edge_connectivity(graph)

    # Compute minimum degree δ
    delta = min(graph.degree(u) for u in graph.iterNodes())

    # Print results
    print(f"Karger Edge Connectivity: {karger_result}")
    print(f"Min(λ', δ): {min(karger_result, delta)}")
