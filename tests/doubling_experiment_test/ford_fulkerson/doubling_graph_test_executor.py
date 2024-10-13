"""
This script is used to execute the doubling experiment with Ford-Fulkerson algorithm on
the generated simple undirected graphs created by validation_graphs_creator.py, or simply the
ones that are uploaded, stored in local tests_graphs/generated_graphs.
The script runs all the algorithms and saves their results in local results/generated_graphs in a CSV file only
if the check about simple graphs is true.
"""

from tests.graph_test_execution import check_all_graphs, run_ford_fulkerson_on_graphs


if __name__ == '__main__':

    """ FORK-FULKERSON DOUBLING EXPERIMENT TESTS """
    try:

        # input directory
        input_dir = 'test_graphs/generated_graphs'

        print(f"Starting the doubling experiment test with Ford-Fulkerson algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Ford-Fulkerson algorithm...")

            # ford-fulkerson algorithm run
            output_file = 'results/generated_graphs/ford_fulkerson_results.csv'
            run_ford_fulkerson_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")
