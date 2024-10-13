"""
This script is used to validate the Stoer-Wagner algorithm and the Ford-Fulkerson algorithm
 compared to NetworkX edge connectivity algorithm on the generated simple undirected graphs created by
 graphs_creator.py, or simply uploaded, stored in test graphs/generated_graphs.
It runs all the algorithms and saves their results in the results/generated_graphs in a CSV file only
if the check about simple graphs is true.
"""

import os
import time
import pandas as pd
import networkx as nx
from graphs.graph_loader import GraphLoader
from stoer_wagner.stoer_wagner import stoer_wagner
from ford_fulkerson.ford_fulkerson import ford_fulkerson_min_cut


# function that runs Stoer-Wagner algorithm on all graphs in the input directory
def run_stoer_wagner_on_graphs(input_dir, output_file):

    results = []

    # takes all the csv files in the input directory
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # loads the graph
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_weight()

            # number of edges
            num_edges = graph.number_of_edges()

            # executes the algorithm and measures the start time and end time
            start_time = time.time()
            min_cut_value, _ = stoer_wagner(graph)
            end_time = time.time()

            # execution time
            execution_time = end_time - start_time

            # saves the results
            results.append({
                'file_name': graph_file,
                'edge_connectivity': min_cut_value,
                'execution_time': execution_time,
                'num_edges': num_edges
            })

    # creates a dataframe from the results
    df = pd.DataFrame(results)

    # extract the number of nodes from the file names
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # saves the dataframe to the output file
    df.to_csv(output_file, index=False)
    print(f"results saved to {output_file}")


# function that runs Ford-Fulkerson algorithm on all graphs in the input directory
def run_ford_fulkerson_on_graphs(input_dir, output_file):

    results = []

    # takes all the csv files in the input directory
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # loads the graph
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_capacity()

            # number of edges
            num_edges = graph.number_of_edges()

            # executes the algorithm and measures the start time and end time
            start_time = time.time()
            min_cut = ford_fulkerson_min_cut(graph)
            end_time = time.time()

            # execution time
            execution_time = end_time - start_time

            # saves the results
            results.append({
                'file_name': graph_file,
                ' edge_connectivity': min_cut,
                ' execution_time': execution_time,
                'num_edges': num_edges
            })

    # creates a dataframe from the results
    df = pd.DataFrame(results)

    # extract the number of nodes from the file names
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # saves the dataframe to the output file
    df.to_csv(output_file, index=False)
    print(f"results saved to {output_file}")


# function that runs NetworkX Edge Connectivity algorithm on all graphs in the input directory
def run_networkx_edge_connectivity_on_graphs(input_dir, output_file):

    results = []

    # takes all the csv files in the input directory
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # loads the graph
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_weight()

            # number of edges
            num_edges = graph.number_of_edges()

            # executes the algorithm and measures the start time and end time
            start_time = time.time()
            edge_connectivity = nx.edge_connectivity(graph)
            end_time = time.time()

            # execution time
            execution_time = end_time - start_time

            # saves the results
            results.append({
                'file_name': graph_file,
                'edge_connectivity': edge_connectivity,
                'execution_time': execution_time,
                'num_edges': num_edges
            })

    # creates a dataframe from the results
    df = pd.DataFrame(results)

    # extract the number of nodes from the file names
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # saves the dataframe to the output file
    df.to_csv(output_file, index=False)
    print(f"results saved to {output_file}")


# function that checks if the graph is simple and undirected
def is_simple_undirected_graph(G):

    # verifies if the graph is directed
    if G.is_directed():
        print("The graph is directed.")
        return False

    # verifies if the graph contains loops
    if any(G.has_edge(n, n) for n in G.nodes):
        print("The graph contains loops.")
        return False

    # verifies if the graph contains multiple edges between the two same nodes
    if isinstance(G, nx.MultiGraph):
        for u, v in G.edges:
            if G.number_of_edges(u, v) > 1:
                print(f"The graph contains multiple edges between {u} and {v}.")
                return False

    print("The graph is simple and undirected.")
    return True


# function that checks if the graph contains at least one node
def is_not_empty_graph(graph):

    if graph.number_of_nodes() > 0:
        print(f"The graph is not empty.")
        return True
    return False


# function that checks if the graph contains isolated nodes
def is_not_isolated_graph(graph):

    if all(graph.degree(node) > 0 for node in graph.nodes()):
        print(f"The graph is not isolated.")
        return True
    return False


# function that checks if all the graphs in the input directory are: simple and undirected, not empty and not isolated
def check_all_graphs(input_dir):

    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"\nVerifying graph {graph_file}...")

            # loads the graph
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_weight()

            print(f"Graph loaded has {graph.number_of_nodes()} nodes and {graph.number_of_edges()} edges.")

            # verifies if the graph is simple and undirected
            if not is_simple_undirected_graph(graph):
                print(f"Graph {graph_file} is not simple and undirected. Interruption.")
                return False

            if not is_not_empty_graph(graph):
                print(f"Graph {graph_file} is empty. Interruption.")
                return False

            if not is_not_isolated_graph(graph):
                print(f"Graph {graph_file} contains isolated nodes. Interruption.")
                return False

    print("\nAll checks passed.")
    return True


if __name__ == '__main__':

    """ GRAPHS VALIDATION TESTS """

    try:

        # input directory for generated graphs
        input_dir = 'test_graphs/generated_graphs'

        # checks if all the graphs in the input directory are simple and undirected
        if check_all_graphs(input_dir):
            print("\nAll input graphs are simple and undirected, not empty and not isolated. Running algorithms...")

            # networkx edge connectivity algorithm run
            output_file = 'results/generated_graphs/networkx_edge_connectivity_results.csv'
            run_networkx_edge_connectivity_on_graphs(input_dir, output_file)

            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

            # ford-fulkerson algorithm run
            output_file = 'results/generated_graphs/ford_fulkerson_results.csv'
            run_ford_fulkerson_on_graphs(input_dir, output_file)

        else:
            print("Not all input graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")
