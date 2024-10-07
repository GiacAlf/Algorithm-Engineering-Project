class Trim:
    def __init__(self, G, X, delta):
        self.G = G
        self.X = X
        self.delta = delta

    def trim(self):
        trimmed_set = set()
        for node in self.X:
            if self.G.degree(node) >= self.delta:
                trimmed_set.add(node)
        return trimmed_set
