import networkx as nx
import matplotlib.pyplot as plt


def convert_to_networkx(graph):
    """
    Converte un grafo Networkit in un grafo NetworkX per visualizzazione.
    """
    G = nx.Graph()
    for u, v in graph.iterEdges():
        G.add_edge(u, v)
    return G


def contracted_plot_graph(graph, title="Grafo", output_file=None):
    """
    Plotta il grafo utilizzando Matplotlib e lo salva come immagine se viene specificato un file di output.
    """
    plt.figure(figsize=(8, 6))
    nx.draw(graph, with_labels=True, node_color="lightblue", edge_color="gray", node_size=500, font_size=10)
    plt.title(title)
    if output_file:
        plt.savefig(output_file)
    else:
        plt.show()
