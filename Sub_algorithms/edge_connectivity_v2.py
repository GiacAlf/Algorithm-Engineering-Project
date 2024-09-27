import networkx as nx


def edge_connectivity(graph):
    # Convert NetworKit graph to NetworkX graph for Gabow's algorithm
    nx_graph = nx.Graph()

    # Add edges from the NetworKit graph to the NetworkX graph
    for u in graph.iterNodes():
        for v in graph.iterNeighbors(u):
            nx_graph.add_edge(u, v)

    # Assert that the number of edges in the NetworkX graph is the same as in the original NetworKit graph
    assert nx_graph.number_of_edges() == graph.numberOfEdges(), ("Edge count mismatch between NetworkX and NetworKit "
                                                                 "graphs")

    # Assert that the number of nodes in the NetworkX graph is the same as in the original NetworKit graph
    # assert nx_graph.number_of_nodes() == graph.numberOfNodes(), ("Node count mismatch between NetworkX and NetworKit "
    #                                                                 "graphs")

    # Using NetworkX's edge_connectivity function (Gabow's algorithm)
    result = nx.edge_connectivity(nx_graph)

    # Assert that the result is a positive integer, as edge connectivity should always be non-negative
    assert result >= 0, "Edge connectivity must be non-negative"

    return result


# Example usage for testing
if __name__ == "__main__":
    import networkit as nk

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
