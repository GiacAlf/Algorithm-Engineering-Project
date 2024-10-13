"""
This script is used to run the Ford-Fulkerson algorithm on a given graph.
The time complexity of this implementation is O(n^7)
"""

import networkx as nx
from graphs.graph_loader import GraphLoader


def ford_fulkerson_min_cut(G):
    # nodes of G
    nodes = list(G.nodes)

    # initialize minimum cut value
    min_cut_value = float('inf')

    # cut value for each pair of nodes
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            # uses maximum flow algorithm to find maximum flow
            flow_dict = nx.maximum_flow(G, nodes[i], nodes[j], capacity='capacity')

            print(f"Flow result for nodes {nodes[i]} and {nodes[j]}: {flow_dict}")

            # maximum flow value
            flow_value = flow_dict[0]

            print(f"Flow value between {nodes[i]} and {nodes[j]}: {flow_value}")

            min_cut_value = min(min_cut_value, flow_value)

    return min_cut_value


if __name__ == '__main__':

    """ FOR TESTING PURPOSES """

    try:
        # input directory for generated graphs
        file_path = '../graphs/generated_graphs/generated_graph_with_weights.csv'
        loader = GraphLoader(file_path)

        # load the graph from the CSV file
        graph = loader.load_graph_from_csv_with_capacity()

        # assert that the graph is not empty
        assert graph.number_of_nodes() > 0, "The graph must have at least one node"

        # Check for isolated nodes
        assert all(graph.degree(node) > 0 for node in graph.nodes()), "The graph contains isolated nodes"

        # print the number of nodes and edges
        print(f"Graph loaded with {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

        # min cut value
        min_cut = ford_fulkerson_min_cut(graph)

        # print the min cut value
        print(f"Ford-Fulkerson edge connectivity value is: {min_cut}")

    except Exception as e:
        print(f"Error: {e}")
