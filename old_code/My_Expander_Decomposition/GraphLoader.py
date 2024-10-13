import csv
import os
import networkit as nk


# This function loads a graph from a CSV file
def load_graph_from_csv(path):
    # Initialize graph with a minimum number of nodes
    graph = nk.Graph()  # empty graph
    with open(path, 'r') as file:
        reader = csv.reader(file)

        # Adds nodes and edges to the graph
        for row in reader:
            u, v = int(row[0]), int(row[1])
            # Adds nodes if they don't exist
            while graph.numberOfNodes() <= max(u, v):
                graph.addNode()  # add a node
            graph.addEdge(u, v)  # add the edge
    return graph


# This function loads a graph from a METIS file
def load_graph_from_metis(file_path):
    return nk.readGraph(file_path, nk.Format.METIS)


# This function loads a graph from a GML file
def load_graph_from_gml(file_path):
    return nk.readGraph(file_path, nk.Format.GML)


if __name__ == '__main__':
    result_folder = '../../../tests graphs/generated_graphs/'
    graph_file_name = 'generated_graph'

    # Paths for the different formats
    csv_file_path = os.path.join(result_folder, f'{graph_file_name}.csv')
    metis_file_path = os.path.join(result_folder, f'{graph_file_name}.metis')
    gml_file_path = os.path.join(result_folder, f'{graph_file_name}.gml')

    # Load the graph from CSV
    graph_from_csv = load_graph_from_csv(csv_file_path)
    print(f"Loaded graph from CSV: {graph_from_csv.numberOfNodes()} nodes and {graph_from_csv.numberOfEdges()} edges.")

    # Load the graph from METIS
    graph_from_metis = load_graph_from_metis(metis_file_path)
    print(f"Loaded graph from METIS: {graph_from_metis.numberOfNodes()} nodes and {graph_from_metis.numberOfEdges()} edges.")

    # Load the graph from GML
    graph_from_gml = load_graph_from_gml(gml_file_path)
    print(f"Loaded graph from GML: {graph_from_gml.numberOfNodes()} nodes and {graph_from_gml.numberOfEdges()} edges.")
