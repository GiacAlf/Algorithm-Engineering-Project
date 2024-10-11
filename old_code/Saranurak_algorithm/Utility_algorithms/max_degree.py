from graphs.graph_loader import GraphLoader


# calcola delta, ossia il grado minimo di G
class MaxDegreeCalculator:
    def __init__(self, graph):
        self.graph = graph

    def max_degree(self):
        # Calcola il grado minimo di un grafo G
        max_deg = max(self.graph.degree(v) for v in self.graph.iterNodes())
        return max_deg


if __name__ == '__main__':
    # Path del file CSV generato
    file_path = '../../../graphs/generated_graphs/generated_graph.csv'

    # Carica il grafo dal file
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    max_degree_calculator = MaxDegreeCalculator(graph)
    max_degree = max_degree_calculator.max_degree()

    print(f"Il grado massimo del grafo: {max_degree}")
