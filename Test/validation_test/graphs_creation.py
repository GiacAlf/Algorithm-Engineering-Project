import os
import pandas as pd
from Graphs.nk_simple_connected_graph_generator import create_connected_simple_random_graph_with_weights


def generate_and_save_graphs(nodes_list, output_dir):
    # Crea la cartella di output se non esiste
    os.makedirs(output_dir, exist_ok=True)

    for num_nodes in nodes_list:
        print(f"Generating graph with {num_nodes} nodes...")
        # Genera il grafo (modifica questa parte in base al tuo generatore)
        graph = create_connected_simple_random_graph_with_weights(num_nodes)

        # Converti il grafo in un DataFrame per salvare in CSV
        edges = [(u, v, data['weight']) for u, v, data in graph.edges(data=True)]
        df = pd.DataFrame(edges)

        # Salva il grafo in un file CSV
        output_file = os.path.join(output_dir, f"{num_nodes}_nodes.csv")
        df.to_csv(output_file, index=False)
        print(f"Saved graph with {num_nodes} nodes to {output_file}")


# genera dei grafi casuali per i test
if __name__ == '__main__':
    # Parametri di configurazione
    num_graphs = 20  # Numero totale di grafi da generare
    start_nodes = 5  # Nodi di partenza per ogni grafo
    step = 3  # Passo di incremento per ogni grafo
    max_nodes = start_nodes + (num_graphs-1) * step
    nodes_list = [i for i in range(start_nodes, max_nodes, step)]  # Lista di numeri di nodi (es. 5, 6, ..., 14)
    output_dir = 'Graphs/generated_graphs'  # Directory di output
    print(nodes_list)
    generate_and_save_graphs(nodes_list, output_dir)
