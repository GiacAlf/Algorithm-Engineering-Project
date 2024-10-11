def trim(graph, S):
    """
    Removes vertices from set S based on the condition |E(v, S)| < 2 * deg(v) / 5
    :param graph: The Networkit graph
    :param S: The set of nodes S (list of nodes)
    :return: A subset of S after removing vertices
    """
    while True:
        to_remove = []
        for v in S:
            degree_v = graph.degree(v)  # degree of node v
            edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S)  # number of edges between v and nodes in S

            if edges_in_S < 2 * degree_v / 5:
                to_remove.append(v)

        if not to_remove:
            break

        for v in to_remove:
            S.remove(v)

    return S
