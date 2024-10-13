"""
The following code is used to load a graph from a CSV file that can be generated
 by the nx_simple_connected_graph_generator.py script or stored, in that format, by the user.
"""

import csv
import networkit as nk
import networkx as nx


class GraphLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    # function that loads a graph from a CSV file, with true the graph is in NetworkX format
    def load_graph_from_csv(self, use_networkx=True):

        if use_networkx:
            G = nx.Graph()  # NetworkX graph
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    u, v = map(int, row)  # convert from string to int
                    G.add_edge(u, v)
            return G
        else:
            G = nk.Graph()  # NetworKit graph
            with open(self.file_path, mode='r') as file:
                reader = csv.reader(file)
                for row in reader:
                    u, v = map(int, row)  # convert from string to int
                    G.addEdge(u, v)
            return G

    """
    This function is used with Ford-Fulkerson that needs capacity to work.
    Now, for the edge connectivity purpose with unweighted graphs, is preset to 1.
    The graph can be loaded only in NetworkX format because supports capacity
    """

    def load_graph_from_csv_with_capacity(self):

        G = nx.Graph()  # NetworkX graph
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                u, v, capacity = map(int, row)
                G.add_edge(u, v, capacity=capacity)  # adds the capacity
        return G

    """
    This function is used with Stoer-Wagner that needs weight to work.
    Now, for the edge connectivity purpose with unweighted graphs, is preset to 1.
    The graph can be loaded only in NetworkX format because supports capacity
    """

    def load_graph_from_csv_with_weight(self):

        G = nx.Graph()  # NetworkX graph
        with open(self.file_path, mode='r') as file:
            reader = csv.reader(file)
            for row in reader:
                u, v, weight = map(int, row)
                G.add_weighted_edges_from([(u, v, weight)])  # adds the weight
        return G


if __name__ == '__main__':

    """ FOR TESTING PURPOSE """
    """ verifies the loading of a graph from a CSV file """

    # path
    file_path = 'generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)

    # load with NetworkX
    print("Using NetworkX:")
    graph_nx = loader.load_graph_from_csv(True)
    print(f"Number of nodes: {graph_nx.number_of_nodes()}")
    print(f"Number of edges: {graph_nx.number_of_edges()}")

    # load with NetworKit
    print("\nUsing NetworKit:")
    graph_nk = loader.load_graph_from_csv()
    print(f"Number of nodes: {graph_nk.number_of_nodes()}")
    print(f"Number of edges: {graph_nk.number_of_edges()}")
