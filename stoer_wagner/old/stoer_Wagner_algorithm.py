import networkit as nk
import networkx as nx
from graphs.graph_loader import GraphLoader


def stoer_wagner_edge_connectivity(graph):
    # Convertiamo il grafo di Networkit in un grafo di NetworkX
    g_nx = nx.Graph()

    # Aggiungiamo i nodi
    for node in graph.iterNodes():
        g_nx.add_node(node)

    # Aggiungiamo gli archi
    for edge in graph.iterEdges():
        g_nx.add_edge(edge[0], edge[1])

    # Calcola il cut minimo usando l'algoritmo di stoer_wagner
    min_cut_value, partition = nx.stoer_wagner(g_nx)

    return min_cut_value


if __name__ == '__main__':
    # Carica il grafo
    file_path = '../../graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Calcola la connettività degli archi
    k = stoer_wagner_edge_connectivity(graph)

    print(f"stoer_wagner's Edge Connectivity (Deterministic): {k}")
