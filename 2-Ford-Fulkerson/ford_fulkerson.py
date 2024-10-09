import networkx as nx
from Graphs.graph_loader import GraphLoader


def ford_fulkerson_min_cut(G):
    # Trova i nodi del grafo
    nodes = list(G.nodes)

    # Inizializza il valore del cut minimo
    min_cut_value = float('inf')

    # Calcola il valore del cut per ogni coppia di nodi
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            # Usa la funzione maximum_flow senza specificare flow_func
            flow_value, _ = nx.maximum_flow(G, nodes[i], nodes[j])
            min_cut_value = min(min_cut_value, flow_value)

    return min_cut_value


# Main per leggere il grafo dal CSV e calcolare il cut minimo
if __name__ == '__main__':
    try:
        # Path del file CSV contenente il grafo
        file_path = '../Graphs/generated_graphs/generated_graph.csv'
        loader = GraphLoader(file_path)

        # Carica il grafo dal CSV
        graph = loader.load_graph_from_csv_with_capacity(True)

        # Mostra informazioni di base sul grafo caricato
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # Calcola e stampa il valore del minimo cut
        min_cut = ford_fulkerson_min_cut(graph)
        print(f"The Ford-Fulkerson edge connectivity value of the graph is: {min_cut}")

    except Exception as e:
        print(f"Error: {e}")

"""
# Esempio di utilizzo
if __name__ == "__main__":
    # Crea un grafo di esempio
    G = nx.Graph()
    G.add_edges_from([
        (0, 1, {'capacity': 1}),
        (0, 2, {'capacity': 1}),
        (1, 2, {'capacity': 1}),
        (1, 3, {'capacity': 1}),
        (2, 1, {'capacity': 1}),
        (2, 4, {'capacity': 1}),
        (3, 2, {'capacity': 1}),
        (3, 5, {'capacity': 1}),
        (4, 3, {'capacity': 1}),
        (4, 5, {'capacity': 1}),
    ])

    # Calcola il valore del minimum cut
    min_cut_value = ford_fulkerson_min_cut(G)
    print("Valore del minimum cut:", min_cut_value)
"""
