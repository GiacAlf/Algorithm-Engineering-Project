"""
This script is used to validate the Stoer-Wagner algorithm and the Ford-Fulkerson algorithm
 compared to NetworkX edge connectivity algorithm on the generated graphs created by
 generated_graphs_creator.py stored in Test Graphs/generated_graphs.
The script runs all the algorithms and saves their results in the Results/generated_graphs in a CSV file.
"""

import os
import time
import pandas as pd
import networkx as nx
from Graphs.graph_loader import GraphLoader
from Stoer_Wagner.stoer_wagner import stoer_wagner
from Ford_Fulkerson.ford_fulkerson import ford_fulkerson_min_cut


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
            graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

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
    print(f"Results saved to {output_file}")


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
            graph = loader.load_graph_from_csv_with_capacity(use_networkx=True)

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
    print(f"Results saved to {output_file}")


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
            graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

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
    print(f"Results saved to {output_file}")


if __name__ == '__main__':

    """ GENERATED GRAPHS VALIDATION TESTS """

    # input directory for generated graphs
    input_dir = 'Test Graphs/generated_graphs'  # Directory dove sono i grafi di input

    # networkx edge connectivity algorithm run
    output_file = 'Results/generated_graphs/networkx_edge_connectivity_results.csv'
    run_networkx_edge_connectivity_on_graphs(input_dir, output_file)

    # stoer-wagner algorithm run
    output_file = 'Results/generated_graphs/stoer_wagner_results.csv'
    run_stoer_wagner_on_graphs(input_dir, output_file)

    # ford-fulkerson algorithm run
    output_file = 'Results/generated_graphs/ford_fulkerson_results.csv'
    run_ford_fulkerson_on_graphs(input_dir, output_file)
