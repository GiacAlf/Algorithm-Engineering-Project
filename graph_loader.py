import csv
import networkit as nk


class GraphLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_graph_from_csv(self):
        # Inizializza un grafo con un numero sufficiente di nodi
        graph = nk.graph.Graph(0, 0)  # crea un grafo vuoto
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Salta l'intestazione

            # Aggiungi gli archi e i nodi
            for row in reader:
                u, v = int(row[0]), int(row[1])
                # Aggiungi i nodi se non esistono
                while graph.numberOfNodes() <= max(u, v):
                    graph.addNode()  # aggiungi un nodo
                graph.addEdge(u, v)  # ora puoi aggiungere l'arco
        return graph


if __name__ == '__main__':
    file_path = './generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Stampa le informazioni sul grafo caricato
    print(f"Number of nodes: {graph.numberOfNodes()}")
    print(f"Number of edges: {graph.numberOfEdges()}")

