def shave(graph, S):
    """
    Keeps only the nodes that satisfy the condition |E(v, S)| > deg(v) / 2 + 1
    :param graph: The Networkit graph
    :param S: The set of nodes S (list of nodes)
    :return: A subset of S containing nodes that meet the condition
    """
    # Convert the set S to a faster lookup structure (set)
    S_set = set(S)
    result = []

    # Iterate through each node in the set S
    for v in S:
        # Get the degree of node v (number of edges connected to v)
        degree_v = graph.degree(v)

        # Count how many neighbors of v are also in the set S
        edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S_set)

        # Assert that the number of edges in S is non-negative and does not exceed v's degree
        assert 0 <= edges_in_S <= degree_v, \
            f"Invalid number of edges in S for node {v}: {edges_in_S} out of {degree_v}"

        # If the number of edges from v to S exceeds deg(v) / 2 + 1, include v in the result
        if edges_in_S > degree_v / 2 + 1:
            result.append(v)

    # Assert that the result is a subset of the original set S
    assert set(result).issubset(S_set), "The resulting set contains nodes not in the original set S"

    return result
