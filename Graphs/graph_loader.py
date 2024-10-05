"""
the following code is used to load a graph from a CSV file that can be
generated by the graph_generator.py script or prepared by the user
"""
import csv
import networkit as nk


class GraphLoader:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_graph_from_csv(self):
        # initialize graph with a minimum number of nodes
        graph = nk.graph.Graph()  # empty graph
        with open(self.file_path, 'r') as file:
            reader = csv.reader(file)

            # adds nodes and edges to the graph
            for row in reader:
                u, v = int(row[0]), int(row[1])
                # adds nodes if they don't exist
                while graph.numberOfNodes() <= max(u, v):
                    graph.addNode()  # add a node
                graph.addEdge(u, v)  # add the edge
        return graph


if __name__ == '__main__':
    file_path = 'generated_graphs/generated_graph.csv'
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # print the number of nodes and edges
    print(f"Number of nodes: {graph.numberOfNodes()}")
    print(f"Number of edges: {graph.numberOfEdges()}")
