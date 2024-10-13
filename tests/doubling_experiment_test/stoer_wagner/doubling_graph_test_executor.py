"""
This script is used to execute the doubling experiment with Stoer-Wagner algorithm on
the generated simple undirected graphs created by validation_graphs_creator.py, or simply the ones
that are uploaded, stored in local tests_graphs/generated_graphs.
The script runs all the algorithms and saves their results in local results/generated_graphs in a CSV file only
if the check about simple graphs is true.
"""
import os

from tests.graph_test_execution import check_all_graphs, run_stoer_wagner_on_graphs

if __name__ == '__main__':

    output_dir = 'results/generated_graphs'
    # creates the output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)

    """ STOER-WAGNER DOUBLING EXPERIMENT TESTS """
    """TEST 1.1: fixed number of nodes = 64, doubled number of edges"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_1_1'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_1_1.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")

    """TEST 1.2: fixed number of nodes = 128, doubled number of edges"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_1_2'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_1_2.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")

    """TEST 1.3: fixed number of nodes = 256, doubled number of edges"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_1_3'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_1_3.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")

    """TEST 2.1: fixed number of edges = 1024, doubled number of nodes"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_2_1'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_2_1.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")

    """TEST 2.2: fixed number of edges = 1500, doubled number of nodes"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_2_2'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_2_2.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")

    """TEST 2.3: fixed number of edges = 2000, doubled number of nodes"""
    try:
        # input directory
        input_dir = 'test_graphs/generated_graphs_test_2_3'
        print(f"Starting the doubling experiment test with Stoer-Wagner algorithm...")

        # checks if all the graphs in the input directory are simple, undirected, not empty and not isolated
        if check_all_graphs(input_dir):
            print("\nAll input test graphs are simple and undirected, not empty and not isolated. "
                  "Running Stoer-Wagner algorithm...")
            # stoer-wagner algorithm run
            output_file = 'results/generated_graphs/stoer_wagner_results_test_2_3.csv'
            run_stoer_wagner_on_graphs(input_dir, output_file)

        else:
            print("Not all input test graphs are simple and undirected. Execution aborted.")

    except Exception as e:
        print(f"Error: {e}")
