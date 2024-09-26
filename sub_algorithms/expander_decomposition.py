import networkit as nk
from Graphs.graph_loader import GraphLoader


# main class for the first part of the Edge Cut computing
class ExpanderDecomposition:
    def __init__(self, graph, phi):
        self.graph = graph
        self.phi = phi

    def run(self):
        # Esegui la rilevazione delle comunità
        partition = nk.community.detectCommunities(self.graph)
        return partition


if __name__ == '__main__':
    # Carica il grafo dal file CSV
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Esegui expander decomposition
    phi = 0.5  # parametro φ
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # Mostra i risultati della decomposizione
    for subset in partition.getSubsetIds():
        print(f"Subset {subset}: {partition.getMembers(subset)}")
