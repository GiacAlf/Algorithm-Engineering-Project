import networkx as nx
import numpy as np
from scipy.sparse.linalg import cg, LinearOperator, spilu
from scipy.sparse import csr_matrix
import multiprocessing as mp

from Old_Code.simple_connected_graph_generator import create_simple_connected_graph


# Precondizionatore tramite incomplete Cholesky decomposition
def preconditioner_cholesky(G):
    L = nx.laplacian_matrix(G)
    L = csr_matrix(L, dtype=np.float64)
    preconditioner = spilu(L)
    return preconditioner


# Funzione Laplacian solver ottimizzata con precondizionatore
def laplacian_solver_optimized(G, preconditioner=None):
    L = nx.laplacian_matrix(G).astype(float)
    n = L.shape[0]
    b = np.random.rand(n)  # Genera un vettore casuale

    # Definire l'operatore lineare per l'approssimazione iterativa
    def matvec(v):
        return L.dot(v)

    linear_operator = LinearOperator((n, n), matvec=matvec)

    # Usa il metodo di Conjugate Gradient (CG) con precondizionatore, se disponibile
    x, _ = cg(linear_operator, b, M=preconditioner)

    return x


# Funzione per trovare un taglio bilanciato in grafi grandi
def balanced_cut_large_graphs(G, phi, use_metis=True):
    if use_metis:
        import metis
        _, parts = metis.part_graph(G, 2)
        S = [n for n, part in enumerate(parts) if part == 0]
        return set(S)
    else:
        x = laplacian_solver_optimized(G)
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


# Funzione di decomposizione scalabile con parallelizzazione
def expander_decomposition_large(G, phi):
    num_workers = mp.cpu_count()

    # Trova il taglio bilanciato con parallelizzazione
    with mp.Pool(processes=num_workers) as pool:
        cuts = pool.starmap(balanced_cut_large_graphs, [(G.subgraph(c), phi) for c in nx.connected_components(G)])

    # Verifica la proprietà di espansione
    valid_cuts = []
    for cut in cuts:
        if cut and check_expansion(G, cut, phi):
            valid_cuts.append(cut)

    return valid_cuts


# Funzione per verificare l'espansione
def check_expansion(G, S, phi):
    vol_S = sum(G.degree(n) for n in S)
    vol_complement = sum(G.degree(n) for n in set(G.nodes) - S)
    edge_cut = nx.cut_size(G, S)

    return edge_cut / min(vol_S, vol_complement) >= phi


# Convert Networkit Graph to NetworkX Graph
def convert_networkit_to_networknx(nk_graph):
    edges = [(edge.source, edge.target) for edge in nk_graph.edges()]  # Use edges() to get the edges
    return nx.Graph(edges)







# Creiamo un esempio con un grande grafo e testiamo l'algoritmo
def test_expander_decomposition_large():
    nk_graph = create_simple_connected_graph(100)  # Un grafo casuale grande
    G = convert_networkit_to_networknx(nk_graph)  # Converti in NetworkX
    phi = 0.4  # Valore di soglia per l'espansione

    # Usa un precondizionatore per accelerare il solutore Laplaciano
    preconditioner = preconditioner_cholesky(G)

    decompositions = expander_decomposition_large(G, phi)

    for i, dec in enumerate(decompositions):
        print(f"Expander {i + 1}: {dec}")


if __name__ == "__main__":
    test_expander_decomposition_large()
