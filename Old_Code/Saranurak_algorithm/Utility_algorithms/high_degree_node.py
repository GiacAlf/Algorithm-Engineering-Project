from Graphs.graph_loader import GraphLoader


def find_most_connected_node(graph):
    max_degree = -1
    most_connected_node = -1

    for node in graph.iterNodes():
        degree = graph.degree(node)
        if degree > max_degree:
            max_degree = degree
            most_connected_node = node

    return most_connected_node


if __name__ == '__main__':
    # Carica il grafo
    file_path = '../../../Graphs/generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Verifica che il grafo sia stato caricato correttamente
    num_nodes = graph.numberOfNodes()
    num_edges = graph.numberOfEdges()
    print(f"Grafo caricato con {num_nodes} nodi e {num_edges} archi")

    # Trova il nodo più connesso
    start_node = find_most_connected_node(graph)
    print(f"Il nodo più connesso è: {start_node} con grado {graph.degree(start_node)}")