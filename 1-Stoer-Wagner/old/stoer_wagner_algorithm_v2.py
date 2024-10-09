import networkit as nk
import networkx as nx
from Graphs.graph_loader import GraphLoader


def stoer_wagner_edge_connectivity(graph):
    """
    Calcola la connettività degli archi usando l'algoritmo di 1-Stoer-Wagner.

    :param graph: Il grafo di Networkit da cui calcolare la connettività degli archi.
    :return: Il valore del cut minimo.
    """
    # Convertiamo il grafo di Networkit in un grafo di NetworkX
    g_nx = nx.Graph()

    # Aggiungiamo i nodi al grafo NetworkX
    for node in graph.iterNodes():
        g_nx.add_node(node)

    # Aggiungiamo gli archi al grafo NetworkX
    for edge in graph.iterEdges():
        g_nx.add_edge(edge[0], edge[1])

    # Assert che il grafo ha almeno due nodi per calcolare la connettività
    assert g_nx.number_of_nodes() > 1, "Il grafo deve avere almeno due nodi per calcolare la connettività."

    # Calcola il cut minimo usando l'algoritmo di 1-Stoer-Wagner
    min_cut_value, partition = nx.stoer_wagner(g_nx)

    return min_cut_value


if __name__ == '__main__':
    # Carica il grafo dal file CSV
    file_path = '../../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Assicurati che il grafo caricato non sia vuoto
    assert graph.number_of_nodes() > 0, "Il grafo caricato è vuoto."

    # Calcola la connettività degli archi
    k = stoer_wagner_edge_connectivity(graph)

    # Stampa il valore della connettività degli archi calcolato
    print(f"stoer_wagner's Edge Connectivity (Deterministic): {k}")
