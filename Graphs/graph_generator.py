import csv
import networkit as nk
import os


# Questa funzione genera un grafo casuale con num_nodes nodi e num_edges archi
def generate_graph(num_nodes, num_edges):
    graph = nk.generators.ErdosRenyiGenerator(num_nodes, num_edges / (num_nodes * (num_nodes - 1) / 2)).generate()
    return graph


# Questa funzione salva il grafo in un file CSV, senza duplicare gli archi
def save_graph_to_csv(graph, file_path):
    # Controlla se la cartella esiste
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Usa un set per tenere traccia degli archi già scritti
    written_edges = set()

    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        for u in graph.iterNodes():
            for v in graph.iterNeighbors(u):
                # Ordina i nodi in modo che (u, v) e (v, u) siano trattati allo stesso modo
                edge = tuple(sorted((u, v)))

                # Scrive l'arco solo se non è già stato salvato
                if edge not in written_edges:
                    writer.writerow([u, v])
                    written_edges.add(edge)  # Aggiungi l'arco all'insieme


class GraphGenerator:
    def __init__(self, result_folder, file_name):
        self.result_folder = result_folder
        self.file_name = file_name


if __name__ == '__main__':
    result_folder = './generated_graphs'
    file_name = 'generated_graph.csv'
    file_path = os.path.join(result_folder, file_name)

    generator = GraphGenerator(result_folder, file_name)
    graph = generate_graph(4000, 5000)
    save_graph_to_csv(graph, file_path)
