from Graphs.graph_loader import GraphLoader
from Saranurak_algorithm.Sub_algorithms.Expander_Decomposition.CutMatching import CutMatching


class SaranurakEdgeConnectivity:
    def __init__(self):
        pass

    def run_saranurak_algorithm(self, G, phi):
        """
        Esegue l'algoritmo Saranurak Edge Connectivity:
        1. Expander Decomposition
        2. Trim
        3. Shave
        """
        print("Starting Expander Decomposition...")
        expander_sets = self.expander_decomposition(G, phi)  # Step 1: Expander Decomposition

        trimmed_sets = []
        for exp_set in expander_sets:
            print(f"Applying trim on set: {exp_set}")
            trimmed_set = trim(G, exp_set)  # Step 2: Trim

            print(f"Applying shave on trimmed set: {trimmed_set}")
            shaved_set = shave(G, trimmed_set)  # Step 3: Shave

            trimmed_sets.append(shaved_set)

        return trimmed_sets

    def expander_decomposition(self, G, phi):
        """
        Effettua l'expander.pyx decomposition sul grafo G con parametro phi.
        Ritorna un insieme di insiemi A, che sono le partizioni del grafo.
        """
        cut_matching = CutMatching(G, phi, 1, 1)
        A, R, i = cut_matching.cut_matching()

        if i == 0:
            return [set(G.nodes())]
        elif i == 1:
            print("Balanced Cut Returned")
            return self.expander_decomposition(G.degree_preserving_induced_subgraph(list(A)), phi) + \
                   self.expander_decomposition(G.degree_preserving_induced_subgraph(list(R)), phi)
        else:
            print("Unbalanced Cut Returned")
            A_prime = trim(G, A)  # Effettua il trimming in caso di cut sbilanciato
            graph_vertices = set(G.nodes())
            remaining_graph_vertices = graph_vertices - set(A_prime)

            return [A_prime] + self.expander_decomposition(G.degree_preserving_induced_subgraph(list(remaining_graph_vertices)),
                                                           phi)


def trim(graph, S):
    """
    Rimuove i vertici da S se |E(v, S)| < 2 * deg(v) / 5
    :param graph: Il grafo Networkit
    :param S: L'insieme dei nodi (lista di nodi)
    :return: Un sottoinsieme di S dopo la rimozione dei vertici
    """
    while True:
        to_remove = []
        for v in S:
            degree_v = graph.degree(v)  # grado del nodo v
            edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S)  # numero di archi tra v e i nodi in S

            if edges_in_S < 2 * degree_v / 5:
                to_remove.append(v)

        if not to_remove:
            break

        for v in to_remove:
            S.remove(v)

    return S


def shave(graph, S):
    """
    Mantiene solo i nodi che soddisfano la condizione |E(v, S)| > deg(v) / 2 + 1
    :param graph: Il grafo Networkit
    :param S: L'insieme dei nodi (lista di nodi)
    :return: Un sottoinsieme di S contenente i nodi che soddisfano la condizione
    """
    result = []
    for v in S:
        degree_v = graph.degree(v)  # grado del nodo v
        edges_in_S = sum(1 for u in graph.iterNeighbors(v) if u in S)  # numero di archi tra v e i nodi in S

        if edges_in_S > degree_v / 2 + 1:
            result.append(v)

    return result


if __name__ == '__main__':
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Definizione del valore di phi per la decomposizione
    phi = 0.5  # Questo valore può essere modificato in base al grafo e all'applicazione

    saranurak_algo = SaranurakEdgeConnectivity()
    final_sets = saranurak_algo.run_saranurak_algorithm(graph, phi)

    print(f"Final sets after expander.pyx decomposition, trim and shave: {final_sets}")
