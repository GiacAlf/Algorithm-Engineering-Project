import csv
import os
import networkit as nk
import random


# Questa funzione genera un grafo semplice con num_nodes nodi e num_edges archi
def create_simple_connected_graph(num_nodes, num_edges=None):
    min_edges = num_nodes - 1
    max_edges = num_nodes * (num_nodes - 1) // 2

    # Se num_edges non è specificato, scegliamo un valore casuale tra min_edges e max_edges
    if num_edges is None:
        num_edges = random.randint(min_edges, max_edges)
        print(f"Numero di archi non specificato, scelto casualmente tra i valori possibili: {num_edges}")

    # Controlla che il numero di archi sia sufficiente per garantire un grafo connesso
    if num_edges < min_edges:
        raise ValueError("Numero di archi insufficiente per creare un grafo connesso.")

    # Il massimo numero di archi possibili in un grafo semplice non orientato è n(n-1)/2
    if num_edges > max_edges:
        raise ValueError("Numero di archi troppo alto per un grafo semplice con questo numero di nodi.")

    # Creiamo un grafo vuoto con num_nodes nodi
    graph = nk.Graph(num_nodes, weighted=False, directed=False)

    # Prima crea un albero (grafo connesso con esattamente num_nodes - 1 archi)
    nodes = list(range(num_nodes))
    random.shuffle(nodes)

    for i in range(num_nodes - 1):
        # Connetti ogni nodo successivo a un nodo precedente per garantire la connettività
        graph.addEdge(nodes[i], nodes[i + 1])

    # Ora aggiungiamo archi casuali finché non raggiungiamo num_edges
    edges_added = num_nodes - 1  # Abbiamo già aggiunto num_nodes - 1 archi
    while edges_added < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Aggiungi l'arco solo se è un arco semplice (no loop, no archi multipli)
        if u != v and not graph.hasEdge(u, v):
            graph.addEdge(u, v)
            edges_added += 1

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


if __name__ == '__main__':
    result_folder = './generated_graphs'
    file_name = 'generated_graph.csv'
    file_path = os.path.join(result_folder, file_name)

    # Crea il grafo, se non si settano gli archi vengono scelti random
    graph = create_simple_connected_graph(100)

    # Salva il grafo
    save_graph_to_csv(graph, file_path)

    # Mostra alcune informazioni sul grafo
    print(f"Grafo creato con {graph.numberOfNodes()} nodi e {graph.numberOfEdges()} archi.")
