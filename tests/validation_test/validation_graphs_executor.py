"""
This script is used to validate the Stoer-Wagner algorithm and the Ford-Fulkerson algorithm
 compared to NetworkX edge connectivity algorithm on simple undirected graphs created by
 validation_graphs_creator.py, or simply the ones that are uploaded, stored in tests graphs/generated_graphs.
It runs all the algorithms and saves their results in validation_test/results/generated_graphs in 3 different
 CSV file but only if all the simple graphs, undirected, not empty and not isolated checks are true.
"""

from tests.graph_test_execution import check_all_graphs, run_networkx_edge_connectivity_on_graphs, \
    run_stoer_wagner_on_graphs, run_ford_fulkerson_on_graphs


if __name__ == '__main__':

    """ GRAPHS VALIDATION TESTS """

    try:

        # input directory for generated graphs
        input_dir = 'test_graphs/generated_graphs'

        # checks if all the graphs in the input directory are simple and undirected
        if check_all_graphs(input_dir):
            print("\nAll input graphs are simple and undirected, not empty and not isolated. Running algorithms...")

            # networkx edge connectivity algorithm run
            output_file = 'results/generated_graphs/networkx_edge_connectivity_results.csv'
            run_networkx_edge_connectivity_on_graphs(input_dir, output_file)

            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

            # ford-fulkerson algorithm run
            output_file = 'results/generated_graphs/ford_fulkerson_results.csv'
            run_ford_fulkerson_on_graphs(input_dir, output_file)

        else:
            print("Not all input graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")
