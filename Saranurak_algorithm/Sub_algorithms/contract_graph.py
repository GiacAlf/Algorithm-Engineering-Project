import networkit as nk


def contract_graph(graph, partition):
    contracted_graph = nk.Graph(graph.numberOfNodes(), weighted=False)
    supernode_map = {}

    for subset in partition.getSubsetIds():
        members = list(partition.getMembers(subset))  # Convert set to list
        if len(members) > 1:
            supernode = members[0]
            for node in members:
                supernode_map[node] = supernode
        else:
            supernode_map[members[0]] = members[0]

    for u in graph.iterNodes():
        for v in graph.iterNeighbors(u):
            u_contracted = supernode_map[u]
            v_contracted = supernode_map[v]
            if u_contracted != v_contracted:
                contracted_graph.addEdge(u_contracted, v_contracted)

    return contracted_graph
