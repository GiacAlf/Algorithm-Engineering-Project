import networkx as nx


def edge_connectivity(graph):
    # Convert NetworKit graph to NetworkX graph for Gabow's algorithm
    nx_graph = nx.Graph()

    for u in graph.iterNodes():
        for v in graph.iterNeighbors(u):
            nx_graph.add_edge(u, v)

    # Using NetworkX's edge_connectivity function (Gabow's algorithm)
    return nx.edge_connectivity(nx_graph)
