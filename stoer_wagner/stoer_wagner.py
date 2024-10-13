"""
This script is used to run the Stoer-Wagner algorithm on a given graph
The time complexity of the algorithm is O(m*n*log n)
"""

from itertools import islice
import networkx as nx
from networkx.utils import BinaryHeap, arbitrary_element
from graphs.graph_loader import GraphLoader


def stoer_wagner(G, weight="weight", heap=BinaryHeap):
    n = len(G)
    if n < 2:
        raise nx.NetworkXError("graph has less than two nodes.")
    if not nx.is_connected(G):
        raise nx.NetworkXError("graph is not connected.")

    # Make a copy of the graph for internal use
    G = nx.Graph((u, v, {"weight": e.get(weight, 1)}) for u, v, e in G.edges(data=True) if u != v)

    # Disable caching
    G.__networkx_cache__ = None

    for u, v, e in G.edges(data=True):
        if e["weight"] < 0:
            raise nx.NetworkXError("graph has a negative-weighted edge.")

    cut_value = float("inf")
    nodes = set(G)

    # contracted node pairs
    contractions = []

    # Repeatedly pick a pair of nodes to contract until only one node is left
    for i in range(n - 1):
        # Pick an arbitrary node u and create a set A = {u}
        u = arbitrary_element(G)
        A = {u}
        # Repeatedly pick the node "most tightly connected" to A and add it to A
        h = heap()  # min-heap emulating a max-heap
        for v, e in G[u].items():
            h.insert(v, -e["weight"])
        # Repeat until all but one node has been added to A
        for j in range(n - i - 2):
            u = h.pop()[0]
            A.add(u)
            for v, e in G[u].items():
                if v not in A:
                    h.insert(v, h.get(v, 0) - e["weight"])
        # A and the remaining node v define a "cut of the phase"
        v, w = h.min()
        w = -w
        if w < cut_value:
            cut_value = w
            best_phase = i
        # Contract v and the last node added to A
        contractions.append((u, v))
        for w, e in G[v].items():
            if w != u:
                if w not in G[u]:
                    G.add_edge(u, w, weight=e["weight"])
                else:
                    G[u][w]["weight"] += e["weight"]
        G.remove_node(v)

    # Recover the optimal partitioning from the contractions
    G = nx.Graph(islice(contractions, best_phase))
    v = contractions[best_phase][1]
    G.add_node(v)
    reachable = set(nx.single_source_shortest_path_length(G, v))
    partition = (list(reachable), list(nodes - reachable))

    return cut_value, partition


if __name__ == '__main__':

    """ FOR TESTING PURPOSES """

    try:
        # input directory for generated graphs
        file_path = '../graphs/generated_graphs/generated_graph_with_weights.csv'
        loader = GraphLoader(file_path)

        # load the graph from the CSV file
        graph = loader.load_graph_from_csv_with_weight()

        # assert that the graph is not empty
        assert graph.number_of_nodes() > 0, "The graph must have at least one node"

        # Check for isolated nodes
        assert all(graph.degree(node) > 0 for node in graph.nodes()), "The graph contains isolated nodes"

        # print the number of nodes and edges
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # min cut value
        min_cut_value, _ = stoer_wagner(graph)

        # print the min cut value
        print(f"Stoer-Wagner edge connectivity value is: {min_cut_value}")

    except Exception as e:
        print(f"Error: {e}")
