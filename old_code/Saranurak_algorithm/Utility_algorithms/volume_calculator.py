from graphs.graph_loader import GraphLoader


# calcola il volume del grafo, ossia la sommatoria di tutti i gradi di tutti i vertici in V
class VolumeCalculator:
    def __init__(self, graph):
        self.graph = graph

    def calculate_volume(self):
        # Calcola il volume di tutti i nodi del grafo
        all_nodes = self.graph.iterNodes()  # Ottieni tutti i nodi del grafo
        volume = sum(self.graph.degree(v) for v in all_nodes)
        return volume


if __name__ == '__main__':
    # Path del file CSV generato
    file_path = '../../../graphs/generated_graphs/generated_graph.csv'

    # Carica il grafo dal file
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Calcola il volume di tutti i nodi del grafo
    volume_calculator = VolumeCalculator(graph)
    total_volume = volume_calculator.calculate_volume()

    print(f"Il volume totale del grafo: {total_volume}")
