"""
This script creates a simple connected random graph giving as parameters the number of nodes and edges.
If only the number of nodes is given, it creates a simple connected random graph with random number of edges.
Then it saves the graph as a CSV file.
"""

import csv
import networkx as nx
import random
from graphs_utility_functions.graph_plot import plot_graph


# function that creates a simple connected random graph
def create_connected_simple_random_graph(num_nodes, num_edges=None):

    min_edges = num_nodes - 1
    max_edges = num_nodes * (num_nodes - 1) // 2

    # If num_edges is not specified, choose a random value between min_edges and max_edges
    if num_edges is None:
        num_edges = random.randint(min_edges, max_edges)
        print(f"Number of edges not specified, randomly chosen between possible values: {num_edges}")

    # Check validity of the input
    if num_nodes < 1:
        raise ValueError("The number of nodes must be at least 1.")

    if num_edges < min_edges:
        raise ValueError("The number of edges must be at least num_nodes - 1 to ensure connectivity.")

    if num_edges > max_edges:
        raise ValueError("The number of edges exceeds the maximum for a simple graph.")

    # Create a connected tree to ensure connectivity
    G = nx.random_tree(num_nodes)

    # Add random edges until we reach num_edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Add the edge only if it's a simple edge (no loops, no multiple edges)
        if u != v and not G.has_edge(u, v):
            G.add_edge(u, v)

    return G


# function that creates a simple connected random graph with weights, that can be fixed
# or random in a certain fixed range
def create_connected_simple_random_graph_with_weights(num_nodes, num_edges=None, fixed_weight=None):

    # if fixed_weight is not specified, choose a random value between 1 and 10 for weight
    weight_range = (1, 10)
    min_edges = num_nodes - 1
    max_edges = num_nodes * (num_nodes - 1) // 2

    # if num_edges is not specified, choose a random value between min_edges and max_edges
    if num_edges is None:
        num_edges = random.randint(min_edges, max_edges)
        print(f"Number of edges not specified, chosen randomly between possible values: {num_edges}")

    # Check validity of the input
    if num_nodes < 1:
        raise ValueError("Number of nodes must be at least 1.")

    if num_edges < min_edges:
        raise ValueError("Number of edges must be at least num_nodes - 1 to ensure connectivity.")

    if num_edges > max_edges:
        raise ValueError("Edges number exceeds the maximum for a simple graph.")

    # Create a connected tree to ensure connectivity
    G = nx.random_tree(num_nodes)

    # adds weights to the edges
    for u, v in G.edges():
        weight = fixed_weight if fixed_weight is not None else random.randint(*weight_range)
        G[u][v]['weight'] = weight

    # Add random edges until we reach num_edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Add the edge only if it's a simple edge (no loops, no multiple edges)
        if u != v and not G.has_edge(u, v):
            weight = fixed_weight if fixed_weight is not None else random.randint(*weight_range)
            G.add_edge(u, v, weight=weight)

    return G


# function that saves the graph to a CSV file
def save_graph_to_csv(graph, file_path):

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for u, v in graph.edges():
            writer.writerow([u, v])
    print(f"Graph saved to {file_path}.")


# function that saves the graph with weights to a CSV file
def save_graph_with_weights_to_csv(graph, file_path):

    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Node1', 'Node2', 'Weight'])  # uncomment this line for having the header in CSV file
        for u, v, data in graph.edges(data=True):
            weight = data['weight']
            writer.writerow([u, v, weight])
    print(f"Graph with weights saved to {file_path}.")


if __name__ == '__main__':

    """ FOR TESTING PURPOSES """

    try:
        # User inputs
        num_nodes = int(input("Enter the number of nodes: "))
        num_edges = input("Enter the number of edges (leave blank for default): ")
        num_edges = int(num_edges) if num_edges else None

        # create the connected simple random graph with weights
        G_with_weights = create_connected_simple_random_graph_with_weights(num_nodes, num_edges, 1)

        # prints
        print(f"Graph created with {G_with_weights.number_of_nodes()} "
              f"nodes and {G_with_weights.number_of_edges()} edges.")

        # save the graph with weights to CSV
        save_graph_with_weights_to_csv(G_with_weights, 'generated_graphs/generated_graph_with_weights.csv')

        # plot the graph
        plot_graph(G_with_weights)

    except ValueError as e:
        print(e)
