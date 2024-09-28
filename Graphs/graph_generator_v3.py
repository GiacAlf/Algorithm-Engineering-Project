import csv
import networkit as nk
import os


# This function generates a random graph with num_nodes nodes and num_edges edges
def generate_graph(num_nodes, num_edges):
    # Create an Erdos-Renyi graph generator
    graph = nk.generators.ErdosRenyiGenerator(num_nodes, num_edges / (num_nodes * (num_nodes - 1) / 2)).generate()
    return graph


# This function saves the graph to a CSV file
def save_graph_to_csv(graph, file_path):
    # Ensure the folder exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Write the graph to a CSV file
    with open(file_path, mode="w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["source", "target"])  # Column names

        # Collect edges and write them to the file
        edges = [(u, v) for u in graph.iterNodes() for v in graph.iterNeighbors(u)]
        writer.writerows(edges)  # Write all edges at once


class GraphGenerator:
    def __init__(self, result_folder, file_name):
        self.result_folder = result_folder
        self.file_name = file_name


if __name__ == '__main__':
    result_folder = './generated_graphs'
    file_name = 'generated_graph.csv'
    file_path = os.path.join(result_folder, file_name)

    generator = GraphGenerator(result_folder, file_name)
    graph = generate_graph(10, 20)  # Example: 10 nodes, 20 edges
    save_graph_to_csv(graph, file_path)
