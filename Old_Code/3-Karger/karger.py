import random

def karger_min_cut(graph):
    # Creare una copia del grafo
    G = {u: set(adj) for u, adj in graph.items()}

    while len(G) > 2:
        # Scegliere un arco casuale
        u = random.choice(list(G.keys()))
        v = random.choice(list(G[u]))

        # Unire i nodi u e v in un nuovo nodo
        G[u].update(G[v])  # Aggiungi i vertici adiacenti di v a u

        # Aggiornare gli adiacenti di u
        for x in list(G[v]):
            if x != u:  # Non aggiungere u stesso
                G[x].remove(v)  # Rimuovi v dagli adiacenti di x
                G[x].add(u)     # Aggiungi u agli adiacenti di x

        # Rimuovi il nodo v
        del G[v]

    # Restituisci il numero di archi rimanenti (cut)
    return sum(len(adj) for adj in G.values()) // 2

# Esempio di utilizzo
if __name__ == "__main__":
    # Creare un grafo di esempio
    graph = {
        0: {1, 2},
        1: {0, 2, 3},
        2: {0, 1, 3},
        3: {1, 2, 4, 5},
        4: {3, 5},
        5: {3, 4},
    }

    num_trials = 100  # Numero di prove per ottenere un cut minimo
    min_cut = float('inf')

    for _ in range(num_trials):
        cut_value = karger_min_cut(graph)
        min_cut = min(min_cut, cut_value)

    print(f"Global Minimum Cut: {min_cut}")
