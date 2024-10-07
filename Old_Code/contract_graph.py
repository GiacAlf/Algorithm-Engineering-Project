import networkit as nk


def contract_graph(graph, partition):
    """
    Questa funzione contrae il grafo `graph` sulla base della partizione fornita.
    Ogni insieme della partizione viene contratto in un singolo nodo.
    """
    contracted_graph = nk.Graph(graph.upperEdgeIdBound(), weighted=False, directed=False)

    # Crea una mappatura nodo -> supernodo basata sulla partizione
    node_to_supernode = {}
    for subset in partition.getSubsetIds():
        members = partition.getMembers(subset)
        supernode = members[0]  # Rappresentiamo il supernodo con uno dei nodi dell'insieme
        for node in members:
            node_to_supernode[node] = supernode

    # Aggiungi archi tra i supernodi nel grafo contratto
    for u, v in graph.iterEdges():
        super_u = node_to_supernode[u]
        super_v = node_to_supernode[v]
        if super_u != super_v:  # Evita i loop
            contracted_graph.addEdge(super_u, super_v)

    return contracted_graph
