import csv
import os
import networkit as nk
import random


# This function generates a simple connected graph with num_nodes nodes and num_edges edges
def create_simple_connected_graph(num_nodes, num_edges=None):
    min_edges = num_nodes - 1
    max_edges = num_nodes * (num_nodes - 1) // 2

    # If num_edges is not specified, choose a random value between min_edges and max_edges
    if num_edges is None:
        num_edges = random.randint(min_edges, max_edges)
        print(f"Number of edges not specified, randomly chosen between possible values: {num_edges}")

    # Check that the number of edges is sufficient to guarantee a connected graph
    if num_edges < min_edges:
        raise ValueError("Insufficient number of edges to create a connected graph.")

    # The maximum number of possible edges in an undirected simple graph is n(n-1)/2
    if num_edges > max_edges:
        raise ValueError("Number of edges too high for a simple graph with this number of nodes.")

    # Create an empty graph with num_nodes nodes
    graph = nk.Graph(num_nodes, weighted=False, directed=False)

    # First create a tree (connected graph with exactly num_nodes - 1 edges)
    nodes = list(range(num_nodes))
    random.shuffle(nodes)

    for i in range(num_nodes - 1):
        # Connect each subsequent node to a previous node to ensure connectivity
        graph.addEdge(nodes[i], nodes[i + 1])

    # Now add random edges until we reach num_edges
    edges_added = num_nodes - 1  # We have already added num_nodes - 1 edges
    while edges_added < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Add the edge only if it's a simple edge (no loops, no multiple edges)
        if u != v and not graph.hasEdge(u, v):
            graph.addEdge(u, v)
            edges_added += 1

    return graph


# This function saves the graph in CSV format, without duplicating edges
def save_graph_to_csv(graph, file_path):
    if os.path.exists(file_path):
        print(f"Warning: {file_path} already exists. It will be overwritten.")
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    written_edges = set()

    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        for u in graph.iterNodes():
            for v in graph.iterNeighbors(u):
                edge = tuple(sorted((u, v)))
                if edge not in written_edges:
                    writer.writerow([u, v])
                    written_edges.add(edge)
    print(f"Saved graph to {file_path}.csv")


# This function saves the graph in METIS format
def save_graph_to_metis(graph, file_path):
    if os.path.exists(file_path):
        print(f"Warning: {file_path} already exists. It will be overwritten.")
    nk.writeGraph(graph, file_path, nk.Format.METIS)
    print(f"Saved graph to {file_path}.metis")


# This function saves the graph in GML format
def save_graph_to_gml(graph, file_path):
    if os.path.exists(file_path):
        print(f"Warning: {file_path} already exists. It will be overwritten.")
    nk.writeGraph(graph, file_path, nk.Format.GML)
    print(f"Saved graph to {file_path}.gml")


if __name__ == '__main__':
    result_folder = './generated_graphs'
    graph_file_name = 'generated_graph'
    csv_file_path = os.path.join(result_folder, f'{graph_file_name}.csv')
    metis_file_path = os.path.join(result_folder, f'{graph_file_name}.metis')
    gml_file_path = os.path.join(result_folder, f'{graph_file_name}.gml')

    # Create the graph, if edges are not set they are chosen randomly
    graph = create_simple_connected_graph(10)

    # Save the graph in different formats
    save_graph_to_csv(graph, csv_file_path)
    save_graph_to_metis(graph, metis_file_path)
    save_graph_to_gml(graph, gml_file_path)

    # Show some information about the graph
    print(f"Graph created with {graph.numberOfNodes()} nodes and {graph.numberOfEdges()} edges.")
