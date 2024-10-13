"""
This script is used to plot a graph from a CSV file using three sub-functions:
create_graph_from_csv, convert_to_networkx, plot_graph
"""

import networkit as nk
import networkx as nx
import matplotlib.pyplot as plt


# creates a graph from a CSV file
def create_graph_from_csv(file_path):
    reader = nk.graphio.EdgeListReader(separator=',', firstNode=0, directed=False)
    graph = reader.read(file_path)
    return graph


# converts a graph into a NetworkX graph
def convert_to_networkx(graph):
    G_nx = nx.Graph()
    for u in range(graph.numberOfNodes()):
        for v in graph.iterNeighbors(u):
            G_nx.add_edge(u, v)
    return G_nx


# plots the graph
def plot_graph(G_nx):
    pos = nx.spring_layout(G_nx)
    nx.draw(G_nx, pos, with_labels=True, node_color='lawngreen', edge_color='lightgray', node_size=300, font_size=8)
    plt.title("Visualizzazione del Grafo")
    plt.show()


if __name__ == '__main__':

    """" FOR TESTING PURPOSE """

    # path
    file_path = 'generated_graphs/generated_graph.csv'

    # load graph
    graph = create_graph_from_csv(file_path)

    # convert to NetworkX
    G_nx = convert_to_networkx(graph)

    # plot graph
    plot_graph(G_nx)
