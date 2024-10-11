import networkit as nk
from graphs.graph_loader import GraphLoader
from old_code.Saranurak_algorithm.Utility_algorithms.calculate_delta import DeltaCalculator
from old_code.Saranurak_algorithm.Utility_algorithms.high_degree_node import find_most_connected_node
from itertools import combinations


class ExpanderDecomposition:
    def __init__(self, graph, phi, start_node):
        self.graph = graph
        self.phi = phi
        self.start_node = start_node

    def run(self):
        # Esegui la rilevazione delle comunità senza specificare il metodo
        partition = nk.community.detectCommunities(self.graph)

        # (Facoltativo) Stampa la partizione
        print("Partizione delle comunità rilevate:")
        for subset in partition.getSubsetIds():
            print(f"Subset {subset}: {partition.getMembers(subset)}")

        return partition

    def edge_boundary(self, S, complement):
        """Calcola il numero di archi che attraversano tra S e il suo complementare."""
        edge_boundary_count = 0
        for u in S:
            for v in self.graph.iterNeighbors(u):
                if v in complement:
                    edge_boundary_count += 1
        return edge_boundary_count

    def calculate_volume_subset(self, subset):
        """Calcola il volume di un sottoinsieme di nodi."""
        return sum(self.graph.degree(v) for v in subset)

    def verify_expansion_properties(self, X_partitions):
        """Verifica la proprietà di espansività interna di ogni partizione X_i."""
        for X_i in X_partitions:
            # Ottieni i membri del sottoinsieme usando partition.getMembers(X_i)
            nodes_in_X_i = set(partition.getMembers(X_i))

            for S in self.subsets(nodes_in_X_i):
                if S:
                    complement_in_X_i = nodes_in_X_i - set(S)
                    edge_cut = self.edge_boundary(S, complement_in_X_i)

                    vol_S = self.calculate_volume_subset(S)
                    vol_complement = self.calculate_volume_subset(complement_in_X_i)

                    if edge_cut < self.phi * min(vol_S, vol_complement):
                        print(f"Warning: Expansion property violated in set {S}.")
                        print(f"  Edge cut: {edge_cut}, vol_S: {vol_S}, vol_complement: {vol_complement}")
                        print(f"  Expansion threshold: {self.phi * min(vol_S, vol_complement)}")

    def subsets(self, X):
        """Genera tutti i sottoinsiemi di X di dimensione 1 e 2."""
        # Usa combinations per generare sottoinsiemi di dimensione 1 e 2
        result = []
        for i in range(1, 3):  # Sottoinsiemi di dimensione 1 e 2
            result.extend(combinations(X, i))
        return result


if __name__ == '__main__':
    # Carica il grafo
    file_path = '../graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Verifica che il grafo sia stato caricato correttamente
    num_nodes = graph.numberOfNodes()
    num_edges = graph.numberOfEdges()
    print(f"Grafo caricato con {num_nodes} nodi e {num_edges} archi")

    # Calcola delta (minimo grado) per il grafo
    delta_calculator = DeltaCalculator(graph)
    delta = delta_calculator.calculate_delta()
    print(f"Delta (minimo grado) del grafo: {delta}")

    # Calcola phi come 40/delta, se delta è maggiore di zero
    if delta > 0:
        phi = 40 / delta
    else:
        phi = 40  # Imposta un valore predefinito se delta è 0 per evitare divisioni per zero
        print("Delta è zero, phi impostato a 40.")

    print(f"Valore di phi calcolato: {phi}")

    # Trova il nodo più connesso
    start_node = find_most_connected_node(graph)
    print(f"Il nodo più connesso è: {start_node}")

    # Esecuzione della decomposizione expander.pyx con phi parametrizzato
    expander = ExpanderDecomposition(graph, phi, start_node)
    partition = expander.run()

    # Verifica la proprietà di espansione interna
    expander.verify_expansion_properties(partition.getSubsetIds())
