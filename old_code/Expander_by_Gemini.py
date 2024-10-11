import networkx as nx
from graphs.graph_loader import GraphLoader
import networkx as nx


def contract_high_degree_nodes(G, degree_threshold):
    """
    Contracts nodes with degree higher than the threshold.

    Args:
        G: A NetworkX graph.
        degree_threshold: The minimum degree for a node to be contracted.

    Returns:
        A new NetworkX graph with contracted nodes.
    """

    H = nx.Graph()

    # Identify high-degree nodes
    high_degree_nodes = [node for node, degree in G.degree() if degree > degree_threshold]

    # Contract each high-degree node with its neighbors
    for node in high_degree_nodes:
        # Create a new node to represent the contracted node
        new_node = len(H)
        H.add_node(new_node)

        # Connect the new node to the neighbors of the contracted node
        for neighbor in G.neighbors(node):
            H.add_edge(new_node, neighbor)

    return H


def expander(G, phi):
    """
    Implements the expander.pyx decomposition algorithm.

    Args:
        G: A networkx graph.
        phi: The expansion parameter.

    Returns:
        A partition of the vertices of G.
    """

    # Step 1: Contract high-degree nodes (placeholder)
    contracted_graph = contract_high_degree_nodes(G.copy())

    # Step 2: Compute maximum flow
    s, t = list(contracted_graph.nodes)[0], list(contracted_graph.nodes)[-1]
    if s == t:
        raise ValueError("Source and sink nodes cannot be the same")
    flow_value, flow_dict = nx.ford_fulkerson_flow(contracted_graph, s, t)

    # Step 3: Partition based on flow values
    partition = {}
    for node, value in flow_dict.items():
        if node == s:
            continue
        partition[node] = "source" if value == flow_value else "sink"

    # Step 4: Verify properties (not implemented yet)
    # Implement edge cut and expansion property verification here

    # Assuming verification is successful, return the partition
    return partition


if __name__ == '__main__':
    file_path = '../graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # print the number of nodes and edges
    print(f"Number of nodes: {graph.numberOfNodes()}")
    print(f"Number of edges: {graph.numberOfEdges()}")

    # Set the expansion parameter (adjust as needed)
    phi = 0.1

    # Run the expander.pyx algorithm
    partition = expander(graph, phi)

    # Print some information about the partition (optional)
    print("Partition:")
    for node, part in partition.items():
        print(f"\tNode {node}: {part}")