import networkx as nx
import numpy as np
from scipy.sparse.linalg import cg  # Conjugate Gradient method for Laplacian solver


# Funzione per calcolare il Laplacian del grafo
def laplacian_solver(G):
    L = nx.laplacian_matrix(G).astype(float)
    b = np.random.rand(L.shape[0])  # Genera un vettore casuale
    # Usa il metodo di Conjugate Gradient (CG) per risolvere il sistema lineare
    x, _ = cg(L, b)
    return x


# Funzione per trovare un taglio bilanciato
def balanced_cut(G, phi):
    # Usa il laplacian solver per ottenere una partizione approssimata
    x = laplacian_solver(G)

    # Usa x per ordinare i nodi e trovare un taglio bilanciato
    sorted_nodes = np.argsort(x)
    best_cut = None
    best_balance = float('inf')

    for i in range(1, len(sorted_nodes)):
        S = set(sorted_nodes[:i])
        vol_S = sum(G.degree(n) for n in S)
        vol_complement = sum(G.degree(n) for n in set(G.nodes) - S)
        edge_cut = nx.cut_size(G, S)
        balance = abs(vol_S - vol_complement)

        if edge_cut / min(vol_S, vol_complement) < phi:
            best_cut = S if balance < best_balance else best_cut
            best_balance = min(balance, best_balance)

    return best_cut


# Funzione per verificare la proprietà di espansione
def check_expansion(G, S, phi):
    vol_S = sum(G.degree(n) for n in S)
    vol_complement = sum(G.degree(n) for n in set(G.nodes) - S)
    edge_cut = nx.cut_size(G, S)

    return edge_cut / min(vol_S, vol_complement) >= phi


# Algoritmo principale di expander decomposition
def expander_decomposition(G, phi):
    # Trova un taglio bilanciato che rispetta la proprietà di espansione
    cut = balanced_cut(G, phi)

    if cut is None:
        print("Expander decomposition non trovata con il phi attuale.")
        return

    # Verifica che la proprietà di espansione sia rispettata
    if check_expansion(G, cut, phi):
        print("Expander decomposition trovata.")
        # Restituisci i sottoinsiemi
        S = set(cut)
        complement = set(G.nodes) - S
        return S, complement
    else:
        print("La proprietà di espansione è violata.")
        return None


# Creiamo un esempio di grafo e testiamo l'algoritmo
G = nx.gnp_random_graph(10, 0.5)  # Un piccolo grafo casuale
phi = 0.4  # Valore di espansione

S, complement = expander_decomposition(G, phi)

if S is not None:
    print(f"Subset S: {S}")
    print(f"Subset complement: {complement}")
else:
    print("Nessuna decomposizione trovata.")
