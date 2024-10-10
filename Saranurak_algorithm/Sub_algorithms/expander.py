import networkx as nx
import random

from Graphs.graph_plot import plot_graph, convert_to_networkx
from Old_Code.My_Expander_Decomposition.GraphLoader import load_graph_from_csv
from Graphs.nx_simple_connected_graph_generator import create_connected_simple_random_graph


def trim(A, graph, degree_threshold=2):
    """
    Funzione di trimming che rimuove i nodi con un grado inferiore alla soglia.
    """
    trimmed_A = set([node for node in A if graph.degree(node) >= degree_threshold])
    return trimmed_A


class ExpanderDecomposition:
    def __init__(self, graph):
        self.graph = graph

    def cut_matching(self):
        """
        Implementazione semplificata del cut-matching che divide il grafo in due gruppi.
        Qui utilizziamo un'euristica casuale per separare i nodi.
        """
        nodes = list(self.graph.nodes)
        random.seed(42)
        # Ordina i nodi per grado (per esempio, puoi prendere quelli con grado più basso per A)
        nodes_sorted_by_degree = sorted(nodes, key=lambda node: self.graph.degree(node))

        mid = len(nodes) // 2
        A = nodes_sorted_by_degree[:mid]
        R = nodes_sorted_by_degree[mid:]

        return A, R

    def decompose(self, phi):
        A, R = self.cut_matching()

        # stampa A e R per verifica, stampa ok il cut_matching
        print("A:", A)
        print("R:", R)

        if len(A) == 0 or len(R) == 0:
            return [set(self.graph.nodes)]

        A_prime = trim(A, self.graph)

        # stampa A_prime per verifica, stampa ok il trim
        print("A_prime:", A_prime)

        # Se il trimming rimuove tutti i nodi, fermiamo la decomposizione
        if len(A_prime) == 0:
            return [set(A)]  # Restituisce il gruppo corrente

        remaining_vertices = set(self.graph.nodes) - A_prime

        subgraph_A = self.graph.subgraph(A_prime)
        subgraph_R = self.graph.subgraph(remaining_vertices)

        # Ricorsione su ciascun sotto-grafo
        return ExpanderDecomposition(subgraph_A).decompose(phi) + ExpanderDecomposition(subgraph_R).decompose(phi)


"""
# per capire se lo carica bene, lo fà
def print_graph(graph):
    print(f"Nodes: {list(graph.iterNodes())}")
    print("Edges:")
    for u in graph.iterNodes():
        for v in graph.iterNeighbors(u):
            if u < v:  # Per evitare di stampare gli archi due volte
                print(f"{u} -- {v}")
"""

# Esempio di utilizzo
if __name__ == "__main__":
    # Crea un grafo di esempio con 10 nodi e 15 archi
    # num_nodes = 10
    # num_edges = 15
    # G = create_connected_simple_random_graph(num_nodes, num_edges)

    # Load the graph from CSV
    file_path = '../../Graphs/generated_graphs/generated_graph.csv'
    G = load_graph_from_csv(file_path)

    # Stampa il grafo caricato a terminale
    # print_graph(G)

    # conversione per far funzionare il grafo caricato
    G_nx = convert_to_networkx(G)

    # plot a schermo
    plot_graph(G_nx)

    # Imposta il valore di phi (conduttanza)
    """
    si considera un insieme S e si calcola:
     
    phi(S)= # archi che attraversano il cut / min(volume(S), volume(S complementare))
     
    il volume di S sono gli archi di S ma non quelli che sono stati contati nel cut
    il volume del complementare di S include solo archi che non sono già stati contati nel volume di S
    """
    phi = 0.5

    # Esegui la decomposizione dell'expander
    expander = ExpanderDecomposition(G_nx)
    result = expander.decompose(phi)

    print("Risultato della decomposizione dell'expander:", result)
