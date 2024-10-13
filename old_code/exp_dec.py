import networkit as nk
from graphs_utility_functions.graph_loader import GraphLoader
from old_code.Saranurak_algorithm.Utility_algorithms.high_degree_node import find_most_connected_node
from old_code.Saranurak_algorithm.Utility_algorithms.calculate_delta import DeltaCalculator

"""
class ExpanderDecomposition:
    def __init__(self, graph, phi, start_node):
        self.graph = graph
        self.phi = phi
        self.start_node = start_node

    def run(self):
        # Esegui la rilevazione delle comunità
        partition = nk.community.detectCommunities(self.graph)

        # (Facoltativo) Stampa la partizione
        print("Partizione delle comunità rilevate:")
        for subset in partition.getSubsetIds():
            print(f"Subset {subset}: {partition.getMembers(subset)}")

        return partition
"""


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


if __name__ == '__main__':
    # Carica il grafo
    file_path = '../graphs_utility_functions/generated_graphs/generated_graph.csv'

    # Carica il grafo dal file
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Verifica che il grafo sia stato caricato correttamente
    num_nodes = graph.numberOfNodes()
    num_edges = graph.numberOfEdges()
    print(f"Grafo caricato con {num_nodes} nodi e {num_edges} archi")

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
