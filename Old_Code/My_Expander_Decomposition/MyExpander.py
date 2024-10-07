import networkit as nk
from networkit import Graph

from Saranurak_algorithm.Sub_algorithms.My_Expander_Decomposition.CutMathcing import CutMatching
from Saranurak_algorithm.Sub_algorithms.My_Expander_Decomposition.GraphLoader import load_graph_from_csv


class ExpanderDecomposition:
    def __init__(self):
        pass

    def get_subgraph(G, node_set):
        subgraph = Graph(len(node_set), weighted=G.isWeighted())
        node_map = {node: idx for idx, node in enumerate(node_set)}

        for u in node_set:
            for v in G.iterNeighbors(u):
                if v in node_set:
                    subgraph.addEdge(node_map[u], node_map[v], G.weight(u, v))

        return subgraph

    # Utilizza Networkit per le performance ma converte a NetworkX dove necessario
    def find_cut(self, G):
        # Se G è un grafo di Networkit, convertilo in NetworkX
        if isinstance(G, nk.graph.Graph):
            G_nx = nk.nxadapter.nk2nx(G)
            nodes = list(G_nx.nodes())
        else:
            nodes = list(G.nodes())

        # Rest of your cut-finding logic using 'nodes' remains unchanged

    def decomposition(self, G, phi):
        cut_matching = CutMatching(G, phi, 100, 0.1)
        A, R, i = cut_matching.cut_matching()

        if i == 0:
            # Utilizza G in formato NetworkX per ottenere i nodi
            if isinstance(G, nk.graph.Graph):
                G_nx = nk.nxadapter.nk2nx(G)
                return [set(G_nx.nodes())]
            else:
                return [set(G.nodes())]  # Return the full graph if no cut was found

        elif i == 1:
            # Balanced cut, recursively decompose both sides
            return self.decomposition(G.subgraph(A), phi) + self.decomposition(G.subgraph(R), phi)

        else:
            # Unbalanced cut, trim A and recurse on remaining graph
            A_prime = trim()
            remaining_vertices = set(G_nx.nodes()) - A_prime if isinstance(G, nk.graph.Graph) else set(G.nodes()) - A_prime
            return [A_prime] + self.decomposition(G.subgraph(remaining_vertices), phi)


# Resto del codice principale rimane invariato

if __name__ == "__main__":
    file_path = '../../Graphs/generated_graphs/generated_graph.csv'

    # Load the graph from CSV (presuppone che la funzione carichi in Networkit)
    graph = load_graph_from_csv(file_path)

    # Set the conductance threshold (phi)
    phi = 0.5

    # Perform the expander.pyx decomposition
    expander_decomposition = ExpanderDecomposition()
    decomposition_result = expander_decomposition.decomposition(graph, phi)

    # Output the result
    print("Expander Decomposition Result:", decomposition_result)
