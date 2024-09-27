import networkit as nk
import networkx as nx
import random
import time


def karger_edge_connectivity(graph):
    """
    Karger's algorithm to compute the edge connectivity of a graph.
    The algorithm randomly contracts edges until only two nodes remain.

    :param graph: The Networkit graph from which to compute edge connectivity.
    :return: The number of edges in the contracted graph (minimum cut).
    """
    # Create a new NetworkX graph from the Networkit graph
    g = nx.Graph()

    # Add nodes and edges from the Networkit graph
    for node in graph.iterNodes():
        g.add_node(node)
    for edge in graph.iterEdges():
        g.add_edge(edge[0], edge[1])

    n = g.number_of_nodes()

    # Assert that the graph has at least two nodes to perform edge contraction
    assert n > 1, "Graph must have at least two nodes for edge connectivity calculation."

    # Continue until only two nodes remain
    while g.number_of_nodes() > 2:
        edges_list = list(g.edges())
        print(f"Available edges for contraction: {edges_list}")  # Debug print

        # Check if there are any edges left
        if len(edges_list) == 0:
            raise ValueError("No edges left to contract. Graph may be disconnected or too reduced.")

        # Randomly select an edge
        u, v = random.choice(edges_list)

        # Merge the two vertices
        g = nx.contracted_nodes(g, u, v, self_loops=False)
        print(
            f"After contracting edge ({u}, {v}): {g.number_of_nodes()} nodes, {g.number_of_edges()} edges.")  # Debug print

        # If there are no edges left after contraction, break the loop
        if g.number_of_edges() == 0:
            raise ValueError("No edges left in the graph after contraction. Graph may be disconnected or too reduced.")

    # Return the number of edges in the contracted graph (this is the minimum cut)
    return g.number_of_edges()


if __name__ == "__main__":
    # Example: Create a sample graph
    # Load your graph from a CSV or other source here.
    # For demonstration purposes, let's create a small example graph.
    graph = nk.Graph(10, weighted=False)  # Create a simple unweighted graph with 10 nodes
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 0)
    graph.addEdge(0, 4)
    graph.addEdge(1, 4)
    graph.addEdge(2, 5)
    graph.addEdge(5, 6)
    graph.addEdge(6, 7)
    graph.addEdge(7, 8)
    graph.addEdge(8, 9)

    # Detect communities (if needed)
    start_time = time.time()
    # Here you would call your community detection function
    print("Communities detected in {:.5f} [s]".format(time.time() - start_time))

    # Call Karger's edge connectivity function
    try:
        karger_result = karger_edge_connectivity(graph)  # Compute on the contracted graph
        print("Minimum cut (edge connectivity):", karger_result)
    except ValueError as e:
        print("Error during Karger's algorithm:", e)
