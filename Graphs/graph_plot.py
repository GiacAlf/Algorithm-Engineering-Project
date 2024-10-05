import networkit as nk
import networkx as nx
import matplotlib.pyplot as plt


# Crea il grafo da un file CSV
def create_graph_from_csv(file_path):
    reader = nk.graphio.EdgeListReader(separator=',', firstNode=0, directed=False)
    graph = reader.read(file_path)
    return graph


# Funzione per convertire il grafo di Networkit in un grafo di Networkx
def convert_to_networkx(graph):
    G_nx = nx.Graph()
    for u in range(graph.numberOfNodes()):
        for v in graph.iterNeighbors(u):
            G_nx.add_edge(u, v)
    return G_nx


# Funzione per visualizzare il grafo
def plot_graph(G_nx):
    pos = nx.spring_layout(G_nx)  # Posizioni dei nodi
    nx.draw(G_nx, pos, with_labels=True, node_color='lawngreen', edge_color='lightgray', node_size=300, font_size=8)
    plt.title("Visualizzazione del Grafo")
    plt.show()


if __name__ == '__main__':
    # Path al file CSV
    file_path = 'generated_graphs/generated_graph.csv'
    graph = create_graph_from_csv(file_path)

    # Converti in grafo Networkx e visualizzalo
    G_nx = convert_to_networkx(graph)
    plot_graph(G_nx)
