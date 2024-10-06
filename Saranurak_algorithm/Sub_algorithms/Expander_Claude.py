import math
import networkx as nx
import random

from Graphs.simple_connected_graph_generator import create_simple_connected_graph


def calculate_conductance(graph, subset):
    cut_size = nx.cut_size(graph, subset)
    volume = sum(dict(graph.degree(subset)).values())
    if volume == 0:
        return 0
    return cut_size / min(volume, graph.number_of_edges() - volume)


def find_low_conductance_cut(graph, phi):
    n = graph.number_of_nodes()
    best_conductance = float('inf')
    best_cut = set()

    for _ in range(int(n * math.log(n))):  # Numero di tentativi
        start = random.choice(list(graph.nodes()))
        cut = {start}
        frontier = set(graph.neighbors(start))

        while frontier:
            v = random.choice(list(frontier))
            cut.add(v)
            frontier.update(graph.neighbors(v))
            frontier -= cut

            conductance = calculate_conductance(graph, cut)
            if conductance < best_conductance:
                best_conductance = conductance
                best_cut = set(cut)

            if conductance > phi:
                break

    return best_cut, best_conductance


def expander_decomposition(graph, epsilon, phi):
    decomposition = []
    remaining_graph = graph.copy()

    while remaining_graph.number_of_edges() > 0:
        components = list(nx.connected_components(remaining_graph))
        if not components:
            break
        component = max(components, key=len)
        subgraph = remaining_graph.subgraph(component).copy()

        cut, conductance = find_low_conductance_cut(subgraph, phi)

        if conductance >= phi:
            decomposition.append(set(subgraph.nodes()))
            remaining_graph.remove_nodes_from(subgraph.nodes())
        else:
            decomposition.append(cut)
            remaining_graph.remove_nodes_from(cut)

    return decomposition


# Convert Networkit Graph to NetworkX Graph
def convert_networkit_to_networknx(nk_graph):
    edges = [(edge.source, edge.target) for edge in nk_graph.edges()]  # Use edges() to get the edges
    return nx.Graph(edges)


# Esempio di utilizzo
nk_graph = create_simple_connected_graph(100)  # Un grafo casuale grande
G = convert_networkit_to_networknx(nk_graph)
epsilon = 0.1
phi = 0.1

result = expander_decomposition(G, epsilon, phi)
print(f"Numero di componenti nella decomposizione: {len(result)}")
for i, component in enumerate(result):
    print(f"Componente {i+1}: {len(component)} nodi")