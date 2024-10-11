import numpy as np
import networkx as nx

from graphs.graph_loader import GraphLoader


def stoer_wagner(graph):
    n = graph.number_of_nodes()
    min_cut = float('inf')
    best_partition = None

    # Inizializza la matrice delle capacità
    capacity = nx.to_numpy_array(graph, weight='weight')

    for i in range(n - 1):
        # Inizializza i nodi per l'iterazione corrente
        A = []
        weights = np.zeros(n)

        # Consolidamento dei nodi
        for _ in range(n - i):
            # Trova il nodo con il peso massimo
            max_weight = -1
            max_node = -1
            for v in range(n):
                if v not in A and weights[v] > max_weight:
                    max_weight = weights[v]
                    max_node = v

            # Aggiungi il nodo A
            A.append(max_node)

            # Aggiungi i pesi degli archi dal grafo
            for v in range(n):
                if v not in A:  # Solo nodi non ancora consolidati
                    weights[v] += capacity[max_node][v]

        # Il cut corrente è dato dal peso dell'ultimo nodo aggiunto
        last_added_node = A[-1]
        cut_value = 0

        for v in range(n):
            if v not in A:
                cut_value += capacity[last_added_node][v]

        # Aggiorna il cut minimo
        if cut_value < min_cut:
            min_cut = cut_value
            best_partition = A

        # Consolidamento dell'ultimo nodo aggiunto
        if len(A) > 1:
            last_node = A[-2]
            for v in range(n):
                if v != last_node and v != last_added_node:
                    capacity[last_node][v] += capacity[last_added_node][v]
            # Rimuovi l'ultimo nodo dalla matrice di capacità
            capacity[last_added_node] = np.zeros(n)

    return min_cut, best_partition


# Esempio di utilizzo con il tuo GraphLoader
if __name__ == '__main__':
    file_path = '../../graphs/generated_graphs/generated_graph_with_weights.csv'
    loader = GraphLoader(file_path)

    # Carica il grafo con i pesi
    graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

    min_cut_value, partition = stoer_wagner(graph)
    print("Minimum Cut Value:", min_cut_value)
    print("Best Partition:", partition)
