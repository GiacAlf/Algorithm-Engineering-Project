import os
import time
import pandas as pd
import networkx as nx
from Graphs.graph_loader import GraphLoader
from Stoer_Wagner.stoer_wagner import stoer_wagner
from Ford_Fulkerson.ford_fulkerson import ford_fulkerson_min_cut


def run_stoer_wagner_on_graphs(input_dir, output_file):
    results = []

    # Ottieni tutti i file CSV nella cartella input
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # Carica il grafo da file
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

            # Esegui l'algoritmo e misura il tempo di esecuzione
            start_time = time.time()
            min_cut_value, _ = stoer_wagner(graph)
            end_time = time.time()

            # Calcola il tempo di esecuzione
            execution_time = end_time - start_time

            # Salva i risultati
            results.append({
                'file_name': graph_file,
                ' edge_connectivity': min_cut_value,
                ' execution_time': execution_time
            })

    df = pd.DataFrame(results)

    # Estrai i nodi dal nome del file e ordina i risultati in base a questo
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # Salva i risultati in un file CSV
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


def run_ford_fulkerson_on_graphs(input_dir, output_file):
    results = []

    # Ottieni tutti i file CSV nella cartella input
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # Carica il grafo da file
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_capacity(use_networkx=True)

            # Esegui l'algoritmo e misura il tempo di esecuzione
            start_time = time.time()
            min_cut = ford_fulkerson_min_cut(graph)
            end_time = time.time()

            # Calcola il tempo di esecuzione
            execution_time = end_time - start_time

            # Salva i risultati
            results.append({
                'file_name': graph_file,
                ' edge_connectivity': min_cut,
                ' execution_time': execution_time
            })

    df = pd.DataFrame(results)

    # Estrai i nodi dal nome del file e ordina i risultati in base a questo
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # Salva i risultati in un file CSV
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


def run_networkx_edge_connectivity_on_graphs(input_dir, output_file):
    results = []

    # Ottieni tutti i file CSV nella cartella input
    for graph_file in os.listdir(input_dir):
        if graph_file.endswith('.csv'):
            graph_path = os.path.join(input_dir, graph_file)
            print(f"Running algorithm on {graph_file}...")

            # Carica il grafo da file
            loader = GraphLoader(graph_path)
            graph = loader.load_graph_from_csv_with_weight(use_networkx=True)

            # Esegui l'algoritmo e misura il tempo di esecuzione
            start_time = time.time()
            edge_connectivity = nx.edge_connectivity(graph)
            end_time = time.time()

            # Calcola il tempo di esecuzione
            execution_time = end_time - start_time

            # Salva i risultati
            results.append({
                'file_name': graph_file,
                ' edge_connectivity': edge_connectivity,
                ' execution_time': execution_time
            })

    df = pd.DataFrame(results)

    # Estrai i nodi dal nome del file e ordina i risultati in base a questo
    df['num_nodes'] = df['file_name'].apply(lambda x: int(x.split('_')[0]))
    df = df.sort_values(by='num_nodes')

    # salva sul file anche il numero degli archi che equivalgono al numero di righe del file
    df['num_edges'] = df['file_name'].apply(lambda x: int(x.split('_')[1].split('.')[0]))

    # Salva i risultati in un file CSV
    df.to_csv(output_file, index=False)
    print(f"Results saved to {output_file}")


if __name__ == '__main__':

    input_dir = 'Graphs/generated_graphs'  # Directory dove sono i grafi di input

    # comparison algorithm
    output_file = './Results/networkx_edge_connectivity_results.csv'
    run_networkx_edge_connectivity_on_graphs(input_dir, output_file)

    output_file = './Results/stoer_wagner_results.csv'
    run_stoer_wagner_on_graphs(input_dir, output_file)

    output_file = './Results/ford_fulkerson_results.csv'
    run_ford_fulkerson_on_graphs(input_dir, output_file)
