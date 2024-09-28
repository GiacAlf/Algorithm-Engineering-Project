import networkx as nx
import networkit as nk


def edge_connectivity(graph):
    """
    Computes the edge connectivity of a graph using NetworkX's implementation of Gabow's algorithm.
    Converts the input NetworKit graph to a NetworkX graph to utilize the NetworkX algorithm.

    :param graph: The input NetworKit graph
    :return: The edge connectivity of the graph (int)
    """
    # Convert NetworKit graph to NetworkX graph for Gabow's algorithm
    nx_graph = nx.Graph()

    # Efficiently add edges from the NetworKit graph to the NetworkX graph
    edges = [(u, v) for u in graph.iterNodes() for v in graph.iterNeighbors(u) if u < v]  # Avoid duplicates
    nx_graph.add_edges_from(edges)

    # Assert that the number of edges matches between the graphs
    assert nx_graph.number_of_edges() == graph.numberOfEdges(), (
        "Edge count mismatch between NetworkX and NetworKit graphs"
    )

    # Using NetworkX's edge_connectivity function (Gabow's algorithm)
    result = nx.edge_connectivity(nx_graph)

    # Assert that the result is a positive integer, as edge connectivity should always be non-negative
    assert result >= 0, "Edge connectivity must be non-negative"

    return result


# Example usage for testing
if __name__ == "__main__":
    # Create a small test graph in NetworKit
    graph = nk.Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 0)

    # Compute edge connectivity
    connectivity = edge_connectivity(graph)

    # Assert the result is an integer
    assert isinstance(connectivity, int), "Edge connectivity should be an integer"

    print(f"Edge Connectivity: {connectivity}")
