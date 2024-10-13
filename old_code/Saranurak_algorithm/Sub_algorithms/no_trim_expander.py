import random
from graphs_utility_functions.graph_plot import plot_graph, convert_to_networkx
from old_code.My_Expander_Decomposition.GraphLoader import load_graph_from_csv


class ExpanderDecomposition:
    def __init__(self, graph):
        self.graph = graph

    def cut_matching(self):
        nodes = list(self.graph.nodes)
        sorted_nodes = sorted(nodes, key=lambda node: self.graph.degree(node), reverse=True)

        assigned_nodes = set()
        groups = []

        for node in sorted_nodes:
            if node not in assigned_nodes:
                current_group = set()
                self.explore_connected_nodes(node, assigned_nodes, current_group)
                groups.append(current_group)

        remaining_nodes = set(self.graph.nodes) - assigned_nodes
        return groups, remaining_nodes

    def explore_connected_nodes(self, start_node, assigned_nodes, current_group):
        stack = [start_node]

        while stack:
            node = stack.pop()
            if node not in assigned_nodes:
                assigned_nodes.add(node)
                current_group.add(node)

                for neighbor in self.graph.neighbors(node):
                    if neighbor not in assigned_nodes:
                        stack.append(neighbor)

    def has_edges_between(self, group_A, group_R):
        for node_A in group_A:
            for node_R in group_R:
                if self.graph.has_edge(node_A, node_R):
                    return True
        return False

    def decompose(self, phi):
        groups, R = self.cut_matching()

        print(f"Gruppi creati: {groups}")
        print(f"Nodi rimanenti (R): {R}")

        results = []
        for A in groups:
            print(f"Esplorando gruppo A: {A}")
            if len(A) == 0:
                continue

            if self.has_edges_between(A, R):
                results.extend(ExpanderDecomposition(self.graph.subgraph(A)).decompose(phi))

        if len(R) > 0:
            results.append(set(R))

        return results


# Esempio di utilizzo
if __name__ == "__main__":
    file_path = '../../../graphs_utility_functions/generated_graphs/generated_graph.csv'
    G = load_graph_from_csv(file_path)

    G_nx = convert_to_networkx(G)

    plot_graph(G_nx)

    phi = 0.5

    expander = ExpanderDecomposition(G_nx)
    result = expander.decompose(phi)

    print("Risultato della decomposizione dell'expander:", result)
