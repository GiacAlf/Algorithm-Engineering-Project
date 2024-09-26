import csv
import networkit as nk
import os


def generate_graph(num_nodes, num_edges):
    # Genera un grafo casuale con num_nodes nodi e num_edges archi
    graph = nk.generators.ErdosRenyiGenerator(num_nodes, num_edges / (num_nodes * (num_nodes - 1) / 2)).generate()
    return graph


def save_graph_to_csv(graph, file_path):
    # Assicurati che la cartella esista
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["source", "target"])  # intestazioni delle colonne
        for u in graph.iterNodes():  # Usa iterNodes() per ottenere i nodi
            for v in graph.iterNeighbors(u):  # Usa iterNeighbors() per ottenere i vicini
                writer.writerow([u, v])


class GraphGenerator:
    def __init__(self, result_folder, file_name):
        self.result_folder = result_folder
        self.file_name = file_name


if __name__ == '__main__':
    result_folder = './generated_graphs'
    file_name = 'generated_graph.csv'
    file_path = os.path.join(result_folder, file_name)

    generator = GraphGenerator(result_folder, file_name)
    graph = generate_graph(10, 20)  # es: 10 nodi, 20 archi
    save_graph_to_csv(graph, file_path)
