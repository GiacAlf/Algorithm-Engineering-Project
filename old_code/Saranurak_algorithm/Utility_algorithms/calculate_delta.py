from graphs_utility_functions.graph_loader import GraphLoader


# calcola delta, ossia il grado minimo di G
class DeltaCalculator:
    def __init__(self, graph):
        self.graph = graph

    def calculate_delta(self):
        # Calcola il grado minimo di un grafo G
        delta = min(self.graph.degree(v) for v in self.graph.iterNodes())
        return delta


if __name__ == '__main__':
    # Path del file CSV generato
    file_path = '../../../graphs_utility_functions/generated_graphs/generated_graph.csv'

    # Carica il grafo dal file
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Calcola il grado minimo
    delta_calculator = DeltaCalculator(graph)
    delta = delta_calculator.calculate_delta()

    print(f"Il grado minimo del grafo: {delta}")
