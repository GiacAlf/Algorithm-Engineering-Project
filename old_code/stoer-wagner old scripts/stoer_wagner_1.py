import networkx as nx
from matplotlib import pyplot as plt

from graphs_utility_functions.graph_loader import GraphLoader


def stoer_wagner_min_cut(graph):
    def min_cut_phase(graph, A):
        # Perform a minimum cut phase, growing A until the last node
        s = A[-1]
        max_weight = -1
        t = None
        for v in graph.nodes:
            if v not in A:
                weight = sum(graph[u][v]['weight'] for u in A if u in graph[v])
                if weight > max_weight:
                    max_weight = weight
                    t = v
        return t

    min_cut_value = float('inf')
    while len(graph) > 1:
        A = [list(graph.nodes())[0]]  # Start with an arbitrary node
        while len(A) < len(graph):
            t = min_cut_phase(graph, A)
            A.append(t)

        # Minimum cut is the sum of the weights of edges connecting A[-1] to other nodes
        cut_value = sum(graph[A[-2]][A[-1]]['weight'] for u in A[:-1] if A[-1] in graph[A[-2]])
        min_cut_value = min(min_cut_value, cut_value)

        # Merge last two nodes in A into a single node
        s, t = A[-2], A[-1]
        for u in graph[t]:
            if u != s:
                if s in graph[u]:
                    graph[u][s]['weight'] += graph[u][t]['weight']
                else:
                    graph.add_edge(u, s, weight=graph[u][t]['weight'])
        graph.remove_node(t)

    return min_cut_value



# Crea un grafo
G = nx.Graph()

# Aggiungi gli archi con un peso di 1 (puoi modificarlo in base alle tue esigenze)
edges = [
    (0, 38), (0, 82), (1, 36), (2, 32), (2, 75), (2, 85), (2, 73),
    (3, 52), (3, 64), (4, 61), (4, 82), (4, 94), (4, 33), (5, 90),
    (6, 33), (7, 99), (7, 90), (8, 41), (9, 55), (9, 46), (10, 46),
    (10, 45), (11, 61), (12, 47), (13, 75), (13, 95), (14, 76),
    (15, 77), (15, 67), (15, 71), (16, 28), (16, 46), (17, 79),
    (17, 30), (18, 48), (18, 60), (18, 33), (19, 81), (19, 58),
    (20, 63), (20, 87), (21, 35), (21, 54), (21, 88), (22, 88),
    (23, 74), (23, 89), (23, 92), (24, 56), (25, 36), (25, 50),
    (25, 64), (25, 93), (26, 56), (26, 59), (27, 86), (27, 29),
    (28, 51), (28, 68), (29, 73), (29, 92), (30, 91), (30, 77),
    (31, 63), (31, 41), (31, 59), (32, 49), (33, 63), (34, 87),
    (37, 83), (37, 58), (38, 49), (39, 82), (40, 93), (41, 55),
    (42, 65), (42, 66), (43, 59), (44, 96), (44, 90), (45, 63),
    (46, 58), (47, 92), (47, 99), (48, 62), (48, 90), (49, 70),
    (51, 84), (51, 98), (51, 87), (52, 76), (52, 63), (52, 92),
    (53, 69), (55, 95), (57, 60), (58, 98), (59, 97), (60, 65),
    (63, 67), (64, 84), (65, 92), (66, 73), (67, 81), (68, 97),
    (68, 90), (68, 94), (69, 93), (69, 85), (71, 97), (72, 95),
    (73, 87), (76, 96), (76, 94), (77, 78), (80, 96), (80, 85),
    (86, 93), (88, 89), (91, 97)
]

# Aggiungi gli archi con un peso di 1
for edge in edges:
    G.add_edge(edge[0], edge[1], weight=1)  # Assegna un peso di 1 a tutti gli archi

# stampa il grafo
for u, v, data in G.edges(data=True):
    print(f"Edge ({u}, {v}) - weight: {data['weight']}")

min_cut = stoer_wagner_min_cut(G)
print(f"The Stoer-Wagner edge connectivity value of the graph is: {min_cut}")


"""
# Main per leggere il grafo dal CSV e calcolare il minimum cut con Stoer-Wagner
if __name__ == '__main__':
    try:
        # Path del file CSV contenente il grafo
        file_path = '../tests graphs_utility_functions/generated_graphs/generated_graph_with_weights.csv'
        loader = GraphLoader(file_path)

        # Carica il grafo dal CSV con capacità predefinita di 1
        graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

        # Mostra i pesi di tutti gli archi per verificare
        for u, v, data in graph.edges(data=True):
            if 'weight' not in data or data['weight'] is None:
                print(f"Edge ({u}, {v}) - weight missing. Setting default weight of 1.")
                data['weight'] = 1  # Imposta peso predefinito a 1 se non presente o nullo
            else:
                print(f"Edge ({u}, {v}) - weight: {data['weight']}")

        # Mostra informazioni di base sul grafo caricato
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # Calcola e stampa il valore del minimum cut con Stoer-Wagner
        min_cut = stoer_wagner_min_cut(graph)
        print(f"The Stoer-Wagner edge connectivity value of the graph is: {min_cut}")

    except Exception as e:
        print(f"Error: {e}")

"""
"""
# Main per leggere il grafo dal CSV e calcolare il minimum cut con Stoer-Wagner
if __name__ == '__main__':
    try:
        # Path del file CSV contenente il grafo
        file_path = '../tests graphs_utility_functions/generated_graphs/generated_graph.csv'
        loader = GraphLoader(file_path)

        # Carica il grafo dal CSV con capacità predefinita di 1
        graph = loader.load_graph_from_csv_with_capacity(use_networkx=True)

        # Mostra i pesi di tutti gli archi per verificare
        for u, v, data in graph.edges(data=True):
            print(f"Edge ({u}, {v}) - weight: {data.get('weight', 'No weight')}")

        # Verifica che il grafo abbia pesi sugli archi e che i pesi non siano 0
        for u, v in graph.edges:
            if 'weight' not in graph[u][v] or graph[u][v]['weight'] == 0:
                graph[u][v]['weight'] = 1  # Imposta peso predefinito a 1 se non presente o è 0

        # Mostra informazioni di base sul grafo caricato
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # Calcola e stampa il valore del minimum cut con Stoer-Wagner
        min_cut = stoer_wagner_min_cut(graph)
        print(f"The Stoer-Wagner edge connectivity value of the graph is: {min_cut}")

    except Exception as e:
        print(f"Error: {e}")

"""
"""
# Creazione di un grafo non pesato con NetworkX
G = nx.Graph()
edges = [(0, 1, 1), (0, 2, 1), (1, 2, 1), (1, 3, 1), (2, 3, 1)]
G.add_weighted_edges_from(edges)

nx.draw(G, with_labels=True)
plt.show()
# Calcolo del minimum cut
min_cut = stoer_wagner_min_cut(G)
print(f"Minimum cut: {min_cut}")
"""
