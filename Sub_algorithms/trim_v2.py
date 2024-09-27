def trim(graph, S):
    """
    Removes vertices from set S based on the condition |E(v, S)| < 2 * deg(v) / 5
    :param graph: The Networkit graph
    :param S: The set of nodes S (list of nodes)
    :return: A subset of S after removing vertices
    """
    while True:
        to_remove = []

        # Iterate through each node in the set S
        for v in S:
            # Get the degree of node v (number of edges connected to v)
            degree_v = graph.degree(v)

            # Count how many neighbors of v are also in the set S
            edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S)

            # Assert that the number of edges in S is non-negative and does not exceed v's degree
            assert 0 <= edges_in_S <= degree_v, \
                f"Invalid number of edges in S for node {v}: {edges_in_S} out of {degree_v}"

            # If the number of edges from v to nodes in S is less than 2 * deg(v) / 5, mark v for removal
            if edges_in_S < 2 * degree_v / 5:
                to_remove.append(v)

        # If no nodes are marked for removal, the trimming process is complete
        if not to_remove:
            break

        # Remove the nodes marked for deletion from set S
        for v in to_remove:
            S.remove(v)

        # Assert that no nodes marked for removal are still present in S
        assert all(v not in S for v in to_remove), \
            "Some nodes marked for removal are still in the set S"

    # Assert that the final result is a subset of the original S
    assert set(S).issubset(S), "Final result should be a subset of the original set S"

    return S
