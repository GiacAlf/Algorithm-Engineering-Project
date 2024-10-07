import networkit as nk
from Graphs.graph_loader import GraphLoader


# class for the first part of the Edge Cut computing
class ExpanderDecomposition:
    def __init__(self, graph, phi):
        self.graph = graph
        self.phi = phi

    def run(self):
        # computes the partitioning
        partition = nk.community.detectCommunities(self.graph)
        return partition


if __name__ == '__main__':
    # loads the graph
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # execution of expander.pyx decomposition
    phi = 20  # parameter φ
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # prints the results of the decomposition
    for subset in partition.getSubsetIds():
        print(f"Subset {subset}: {partition.getMembers(subset)}")
