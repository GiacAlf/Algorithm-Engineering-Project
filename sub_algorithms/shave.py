def shave(graph, S):
    """
    Keeps only the nodes that satisfy the condition |E(v, S)| > deg(v) / 2 + 1
    :param graph: The Networkit graph
    :param S: The set of nodes S (list of nodes)
    :return: A subset of S containing nodes that meet the condition
    """
    result = []
    for v in S:
        degree_v = graph.degree(v)  # degree of node v
        edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S)  # number of edges between v and nodes in S

        if edges_in_S > degree_v / 2 + 1:
            result.append(v)

    return result
