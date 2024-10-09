import networkx as nx


def stoer_wagner_min_cut(graph):
    def min_cut_phase(graph, A):
        # Perform a minimum cut phase, growing A until the last node
        s = A[-1]
        max_weight = -1
        t = None
        for v in graph.nodes:
            if v not in A:
                weight = sum(graph[u][v]['weight'] for u in A if u in graph[v])
                if weight > max_weight:
                    max_weight = weight
                    t = v
        return t

    min_cut_value = float('inf')
    while len(graph) > 1:
        A = [list(graph.nodes())[0]]  # Start with an arbitrary node
        while len(A) < len(graph):
            t = min_cut_phase(graph, A)
            A.append(t)

        # Minimum cut is the sum of the weights of edges connecting A[-1] to other nodes
        cut_value = sum(graph[A[-2]][A[-1]]['weight'] for u in A[:-1] if A[-1] in graph[A[-2]])
        min_cut_value = min(min_cut_value, cut_value)

        # Merge last two nodes in A into a single node
        s, t = A[-2], A[-1]
        for u in graph[t]:
            if u != s:
                if s in graph[u]:
                    graph[u][s]['weight'] += graph[u][t]['weight']
                else:
                    graph.add_edge(u, s, weight=graph[u][t]['weight'])
        graph.remove_node(t)

    return min_cut_value


# Creazione di un grafo non pesato con NetworkX
G = nx.Graph()
edges = [(0, 1, 3), (0, 2, 1), (1, 2, 1), (1, 3, 4), (2, 3, 2)]
G.add_weighted_edges_from(edges)

# Calcolo del minimum cut
min_cut = stoer_wagner_min_cut(G)
print(f"Minimum cut: {min_cut}")
