class Shave:
    def __init__(self, G, X_prime, phi):
        self.G = G
        self.X_prime = X_prime
        self.phi = phi

    def shave(self):
        shaved_set = set()
        for node in self.X_prime:
            if self.G.degree(node) >= self.phi * len(self.X_prime):
                shaved_set.add(node)
        return shaved_set
