import networkit as nk
from Graphs.graph_loader import GraphLoader


# Algoritmo per calcolare delta (minimo grado tra i nodi, ignorando i nodi isolati)
def calculate_delta(graph):
    # Inizializza delta
    delta = 0
    isolated_nodes = 0

    # Itera su tutti i nodi del grafo
    for node in graph.iterNodes():
        degree = graph.degree(node)
        print(f"Node {node} degree: {degree}")  # Stampa il grado di ogni nodo
        if degree > 0:  # Considera solo i nodi con grado maggiore di zero
            if degree < delta:
                delta = degree
        else:
            isolated_nodes += 1

    if delta == float('inf'):  # Se nessun nodo è stato trovato con grado > 0
        delta = 0

    print(f"Numero di nodi isolati: {isolated_nodes}")
    return delta


if __name__ == '__main__':
    # Carica il grafo
    file_path = '../../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Assicurati che il grafo sia non orientato
    graph.indexEdges()  # Per rimuovere duplicati di archi
    graph = nk.graphtools.toUndirected(graph)  # Converte in grafo non orientato

    # Verifica che il grafo sia stato caricato correttamente
    num_nodes = graph.numberOfNodes()
    num_edges = graph.numberOfEdges()
    print(f"Grafo caricato con {num_nodes} nodi e {num_edges} archi")

    # Calcola delta (minimo grado) per il grafo
    delta = calculate_delta(graph)
    print(f"Delta (minimo grado) del grafo: {delta}")
