def trim(graph, S):
    """
    Removes vertices from set S based on the condition |E(v, S)| < 2 * deg(v) / 5
    :param graph: The Networkit graph
    :param S: The set of nodes S (list of nodes)
    :return: A subset of S after removing vertices
    """
    # Convert S to a set for faster membership checking and removal
    S_set = set(S)

    while True:
        to_remove = set()  # Use a set to track nodes to remove for faster operations

        # Iterate through each node in the set S
        for v in S_set:
            # Get the degree of node v (number of edges connected to v)
            degree_v = graph.degree(v)

            # Count how many neighbors of v are also in the set S
            edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S_set)

            # Assert that the number of edges in S is non-negative and does not exceed v's degree
            assert 0 <= edges_in_S <= degree_v, \
                f"Invalid number of edges in S for node {v}: {edges_in_S} out of {degree_v}"

            # If the number of edges from v to nodes in S is less than 2 * deg(v) / 5, mark v for removal
            if edges_in_S < 2 * degree_v / 5:
                to_remove.add(v)

        # If no nodes are marked for removal, the trimming process is complete
        if not to_remove:
            break

        # Remove the nodes marked for deletion from set S
        S_set.difference_update(to_remove)

        # Assert that no nodes marked for removal are still present in S
        assert all(v not in S_set for v in to_remove), \
            "Some nodes marked for removal are still in the set S"

    # Return the final result as a list
    return list(S_set)
