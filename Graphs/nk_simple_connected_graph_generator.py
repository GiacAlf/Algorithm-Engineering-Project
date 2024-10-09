"""
This creates a simple connected random graph givind number of nodes and edges or
only number of nodes if the number of edges is not specified.
Then it saves the graph as a CSV file
"""

import csv
import networkx as nx
import matplotlib.pyplot as plt
import random


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

    # Step 1: Create a connected tree
    G = nx.random_tree(num_nodes)  # Generate a random tree to ensure connectivity

    # Step 2: Add random edges until we reach num_edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Add the edge only if it's a simple edge (no loops, no multiple edges)
        if u != v and not G.has_edge(u, v):
            G.add_edge(u, v)

    return G


def create_connected_simple_random_graph_with_weights(num_nodes, num_edges=None, fixed_weight=None):
    """
    Crea un grafo semplice connesso con un numero specificato di nodi e archi.
    Ogni arco avrà un peso. Il peso può essere fisso (se fixed_weight è specificato) o casuale entro un range (weight_range).
    """
    # if fixed_weight is not specified, choose a random value between 1 and 10 for weight
    weight_range = (1, 10)
    min_edges = num_nodes - 1
    max_edges = num_nodes * (num_nodes - 1) // 2

    # Se num_edges non è specificato, scegli un valore casuale tra min_edges e max_edges
    if num_edges is None:
        num_edges = random.randint(min_edges, max_edges)
        print(f"Numero di archi non specificato, scelto casualmente tra i valori possibili: {num_edges}")

    # Controllo validità dell'input
    if num_nodes < 1:
        raise ValueError("Il numero di nodi deve essere almeno 1.")
    if num_edges < min_edges:
        raise ValueError("Il numero di archi deve essere almeno num_nodes - 1 per garantire la connettività.")
    if num_edges > max_edges:
        raise ValueError("Il numero di archi supera il massimo per un grafo semplice.")

    # Passo 1: Crea un albero connesso
    G = nx.random_tree(num_nodes)  # Genera un albero casuale per garantire la connettività

    # Aggiungi pesi agli archi dell'albero connesso
    for u, v in G.edges():
        weight = fixed_weight if fixed_weight is not None else random.randint(*weight_range)
        G[u][v]['weight'] = weight

    # Passo 2: Aggiungi archi casuali fino a raggiungere num_edges
    while G.number_of_edges() < num_edges:
        u = random.randint(0, num_nodes - 1)
        v = random.randint(0, num_nodes - 1)

        # Aggiungi l'arco solo se è un arco semplice (no loop, no multi-arco)
        if u != v and not G.has_edge(u, v):
            weight = fixed_weight if fixed_weight is not None else random.randint(*weight_range)
            G.add_edge(u, v, weight=weight)

    return G


def save_graph_to_csv(graph, file_path):
    """Save the graph to a CSV file."""
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        for u, v in graph.edges():
            writer.writerow([u, v])
    print(f"Graph saved to {file_path}.")


def save_graph_with_weights_to_csv(graph, file_path):
    """
    Salva il grafo con i pesi nel file CSV, aggiungendo una colonna per il peso di ogni arco.
    """
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        # writer.writerow(['Node1', 'Node2', 'Weight'])  # Intestazione CSV
        for u, v, data in graph.edges(data=True):
            weight = data['weight']
            writer.writerow([u, v, weight])
    print(f"Graph with weights saved to {file_path}.")


# Main section
if __name__ == '__main__':
    try:
        # User inputs
        num_nodes = int(input("Enter the number of nodes: "))
        num_edges = input("Enter the number of edges (leave blank for default): ")
        num_edges = int(num_edges) if num_edges else None


        # Create the connected simple random graph
        G = create_connected_simple_random_graph(num_nodes, num_edges)

        # Draw the graph
        nx.draw(G, with_labels=True)
        plt.show()

        # Show some information about the graph
        print(f"Graph created with {G.number_of_nodes()} nodes and {G.number_of_edges()} edges.")

        # Save the graph to CSV
        save_graph_to_csv(G, 'generated_graphs/generated_graph.csv')


        # Create the connected simple random graph with weights
        G_with_weights = create_connected_simple_random_graph_with_weights(num_nodes, num_edges, 1)

        # Draw the graph
        nx.draw(G_with_weights, with_labels=True)
        plt.show()

        # Show some information about the graph
        print(f"Graph created with {G_with_weights.number_of_nodes()} "
              f"nodes and {G_with_weights.number_of_edges()} edges.")

        # Save the graph with weights to CSV
        save_graph_with_weights_to_csv(G_with_weights, 'generated_graphs/generated_graph_with_weights.csv')

    except ValueError as e:
        print(e)
