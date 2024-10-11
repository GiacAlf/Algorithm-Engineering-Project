from graphs.graph_loader import GraphLoader
import networkx as nx
from old_code.Saranurak_algorithm.Sub_algorithms.Gabow import Gabow
from Saranurak_algorithm.Sub_algorithms.My_Expander_Decomposition.MyExpander import ExpanderDecomposition
from old_code.Saranurak_algorithm.Sub_algorithms.Shave import Shave
from old_code.Saranurak_algorithm.Sub_algorithms.Trim import Trim


class EdgeConnectivity:
    def __init__(self, G, delta, phi):
        self.G = G
        self.delta = delta
        self.phi = phi

    def compute(self):
        # Step 1: Compute expander.pyx decomposition
        expander_decomp = ExpanderDecomposition()
        X = expander_decomp.decomposition(self.G, self.phi)

        # Step 2: Apply the trim step to each X
        trimmed_X = [Trim(self.G, X_i, self.delta).trim() for X_i in X]

        # Step 3: Apply the shave step to each trimmed X
        shaved_X = [Shave(self.G, X_prime, self.phi).shave() for X_prime in trimmed_X]

        # Step 4: Contract each shaved X'' into a supernode
        contracted_graph = self.contract_graph(shaved_X)

        # Step 5: Compute edge connectivity of the contracted graph using Gabow's algorithm
        gabow = Gabow(contracted_graph)
        lambda_prime = gabow.min_edge_connectivity()

        # Step 6: Compute minimum degree of the original graph
        min_degree = min(dict(self.G.degree()).values())

        # Return min{lambda', delta}
        return min(lambda_prime, self.delta)

    def contract_graph(self, shaved_sets):
        contracted_graph = self.G.copy()

        for X_shaved in shaved_sets:
            if len(X_shaved) > 0:
                supernode = next(iter(X_shaved))  # Pick an arbitrary node to represent the supernode
                for node in X_shaved:
                    if node != supernode:
                        contracted_graph = nx.contracted_nodes(contracted_graph, supernode, node, self_loops=False)

        return contracted_graph


if __name__ == "__main__":
    # Load the graph from CSV
    file_path = '../../graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Set delta and phi parameters
    delta = 40  # Example delta
    phi = 0.5   # Example phi

    # Compute the edge connectivity
    edge_connectivity = EdgeConnectivity(graph, delta, phi)
    result = edge_connectivity.compute()

    print("Minimum of lambda' and delta:", result)
