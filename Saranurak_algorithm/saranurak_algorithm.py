import networkit as nk
from Graphs.graph_loader import GraphLoader
from Saranurak_algorithm.Sub_algorithms.high_node_degree import find_most_connected_node
from Sub_algorithms.calculate_delta import calculate_delta
from Sub_algorithms.exp_dec import ExpanderDecomposition
from Sub_algorithms.trim import trim
from Sub_algorithms.shave import shave
from Sub_algorithms.edge_connectivity import edge_connectivity

# Importa le funzioni di plottaggio dal file separato
from Graphs.contracted_graph_plot import convert_to_networkx, contracted_plot_graph


def contract_graph(graph, partition):
    """
    Questa funzione contrae il grafo `graph` sulla base della partizione fornita.
    Ogni insieme della partizione viene contratto in un singolo nodo.
    """
    # Creiamo un nuovo grafo contratto
    contracted_graph = nk.Graph(graph.upperEdgeIdBound(), weighted=False, directed=False)

    # Mappatura nodo -> supernodo
    node_to_supernode = {}
    supernode_id = 0  # ID per i supernodi nel grafo contratto

    for subset in partition.getSubsetIds():
        members = partition.getMembers(subset)
        # Aggiungi il supernodo (senza argomento)
        contracted_graph.addNode()  # Aggiungi un nodo per ogni supernodo
        supernode = supernode_id  # Rappresenta il supernodo con il suo ID
        node_to_supernode.update({node: supernode for node in members})

        supernode_id += 1  # Incrementa l'ID del supernodo

    # Aggiungi archi tra i supernodi nel grafo contratto
    for u, v in graph.iterEdges():
        super_u = node_to_supernode[u]
        super_v = node_to_supernode[v]
        # Controlla se i supernodi sono differenti (evita loop)
        if super_u != super_v:
            contracted_graph.addEdge(super_u, super_v)  # Aggiungi arco

    return contracted_graph


if __name__ == '__main__':
    # Path al file CSV
    file_path = '../Graphs/generated_graphs/generated_graph.csv'

    # Carica il grafo da CSV usando Networkit
    loader = GraphLoader(file_path)
    graph = loader.load_graph_from_csv()

    # Verifica che il grafo sia stato caricato correttamente
    num_nodes = graph.numberOfNodes()
    num_edges = graph.numberOfEdges()
    print(f"Grafo caricato con {num_nodes} nodi e {num_edges} archi")

    # Calcola delta (minimo grado) per il grafo originale G
    delta = calculate_delta(graph)
    print(f"Delta (minimo grado) del grafo: {delta}")

    # Calcola phi come 40/delta, se delta è maggiore di zero
    if delta > 0:
        phi = 40 / delta
    else:
        phi = 40  # Imposta un valore predefinito se delta è 0 per evitare divisioni per zero
        print("Delta è zero, phi impostato a 40.")

    print(f"Valore di phi calcolato: {phi}")

    # Trova il nodo più connesso
    start_node = find_most_connected_node(graph)
    print(f"Il nodo più connesso è: {start_node}")

    # Step 1: Expander decomposition
    expander = ExpanderDecomposition(graph, phi, start_node)
    partition = expander.run()

    # Step 2: Trim
    trimmed_partitions = [trim(graph, set(partition.getMembers(subset))) for subset in partition.getSubsetIds()]

    # Step 3: Shave
    shaved_partitions = [shave(graph, t) for t in trimmed_partitions]

    # Extra Step: Contract the graph G' to feed into Gabow's algorithm
    contracted_graph = contract_graph(graph, partition)

    # Step 4: Computing edge connectivity using Gabow's algorithm
    print("Calcolo della connettività degli archi con l'algoritmo di Gabow sul grafo contratto...")

    # Calcolo di lambda_prime (connettività degli archi di G') usando Gabow's edge connectivity
    lambda_prime = edge_connectivity(contracted_graph)
    print(f"Lambda prime (connettività degli archi del grafo contratto): {lambda_prime}")

    # Calcolo di delta (grado minimo) del grafo originale G
    delta_original = calculate_delta(graph)  # delta è già calcolato sopra, ma lo ricontrolliamo per sicurezza
    print(f"Delta (grado minimo del grafo originale): {delta_original}")

    # Calcolo del risultato finale come min{lambda_prime, delta}
    result = min(lambda_prime, delta_original)
    print(f"Risultato finale (min{{lambda_prime, delta}}): {result}")

    # Visualizzazione del grafo contratto e salvataggio come immagine
    contracted_graph_nx = convert_to_networkx(contracted_graph)
    contracted_plot_graph(contracted_graph_nx, title="Grafo Contratto", output_file="grafo_contratto.png")
