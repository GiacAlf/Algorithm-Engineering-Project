import networkit as nk
from Graphs.graph_loader import GraphLoader


# Class for the first part of the Edge Cut computing
# Expander decomposition splits the graph into smaller communities
class ExpanderDecomposition:
    def __init__(self, graph, phi):
        # Initialize with the graph and the parameter φ
        self.graph = graph
        self.phi = phi

    def run(self):
        # Computes the partitioning using NetworKit's community detection
        partition = nk.community.detectCommunities(self.graph)

        # Assert that the partition is valid (each node should be assigned to one subset)
        assert partition.numberOfSubsets() > 0, "Partition must have at least one subset"

        # Verify that all nodes are accounted for in the partition
        total_nodes_in_partition = sum(len(partition.getMembers(subset)) for subset in partition.getSubsetIds())
        assert self.graph.numberOfNodes() == total_nodes_in_partition, \
            "Total nodes in the partition must match the number of nodes in the graph"

        return partition


if __name__ == '__main__':
    # Loads the graph from a CSV file
    file_path = '../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Assert that the graph has nodes and edges
    assert graph.numberOfNodes() > 0, "Graph must have at least one node"
    assert graph.numberOfEdges() > 0, "Graph must have at least one edge"

    # Execution of expander decomposition with parameter φ
    phi = 0.5  # Parameter φ
    expander = ExpanderDecomposition(graph, phi)
    partition = expander.run()

    # Prints the results of the decomposition
    for subset in partition.getSubsetIds():
        members = partition.getMembers(subset)

        # Assert that each subset has at least one member
        assert len(members) > 0, f"Subset {subset} is empty"

        print(f"Subset {subset}: {members}")
