import networkit as nk


def contract_graph(graph, partition):
    # Create a new empty graph for the contracted graph, with the same number of nodes as the original graph
    # The graph is unweighted, hence weighted=False
    contracted_graph = nk.Graph(graph.numberOfNodes(), weighted=False)

    # A dictionary to map each node to its corresponding supernode in the contracted graph
    supernode_map = {}

    # Iterate through each subset in the partition
    for subset in partition.getSubsetIds():
        members = list(partition.getMembers(subset))  # Convert set to list for easy access
        # If the subset contains more than one node, choose the first node as the supernode
        if len(members) > 1:
            supernode = members[0]
            for node in members:
                supernode_map[node] = supernode  # Map each node in the subset to the supernode
        else:
            # If the subset contains only one node, it is its own supernode
            supernode_map[members[0]] = members[0]

    # Ensure all nodes in the original graph are mapped to a supernode
    assert all(node in supernode_map for node in graph.iterNodes()), "All nodes must be mapped to a supernode"

    # Add edges to the contracted graph
    for u in graph.iterNodes():
        for v in graph.iterNeighbors(u):
            u_contracted = supernode_map[u]
            v_contracted = supernode_map[v]
            # Add an edge between supernodes if they are not the same
            if u_contracted != v_contracted:
                # Check if the edge already exists before adding
                if not contracted_graph.hasEdge(u_contracted, v_contracted):
                    contracted_graph.addEdge(u_contracted, v_contracted)

    # Assert that the number of edges in the contracted graph is less than or equal to the original graph
    assert contracted_graph.numberOfEdges() <= graph.numberOfEdges(), ("Contracted graph has more edges than the "
                                                                       "original graph")

    # Return the contracted graph
    return contracted_graph


# Example usage for testing
if __name__ == "__main__":
    # Create a small test graph
    graph = nk.Graph(5)
    graph.addEdge(0, 1)
    graph.addEdge(1, 2)
    graph.addEdge(2, 3)
    graph.addEdge(3, 4)
    graph.addEdge(4, 0)

    # Partition where each node is its own subset (no contraction should happen)
    partition = nk.Partition(5)
    partition.allToSingletons()  # Each node is its own subset

    contracted = contract_graph(graph, partition)

    # Ensure the contracted graph has the same number of edges as the original
    assert contracted.numberOfEdges() == graph.numberOfEdges(), ("Contracted graph should have the same number of "
                                                                 "edges as original")

    print("All assertions passed. Contracted graph created successfully.")
