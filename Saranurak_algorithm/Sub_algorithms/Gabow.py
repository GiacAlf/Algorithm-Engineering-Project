import networkx as nx


class Gabow:
    def __init__(self, G):
        self.G = G

    def min_edge_connectivity(self):
        # Find the minimum edge cut using a built-in function in NetworkX
        edge_connectivity = nx.edge_connectivity(self.G)
        return edge_connectivity
