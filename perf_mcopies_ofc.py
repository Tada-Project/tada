"""Benchmarks with perf for the functions in the copies module"""

import sys
import perf

sys.path.insert(0, "/home/gkapfham/working/research/source/speed-surprises")

from speedsurprises.text import copies

CONFIGURATION = ".configuration.txt"
DESCRIPTION_METANAME = "description"
PERF_EXPERIMENT_NAME = "perf_mcopies_ofc"


def bench_copy_function(copy_function, current_chosen_size):
    """Run a copy benchmark for a copy_function and a chosen_size"""
    copy_function(current_chosen_size)


# Example of calling the function under analysis:
# copied_character_string = copies.mcopies_ofc(copies_as_string)

if __name__ == "__main__":
    # read the chosen_size
    filepath = CONFIGURATION
    with open(filepath) as fp:
        chosen_size = fp.readline().replace("\n", "")
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    current_experiment_name = PERF_EXPERIMENT_NAME + str(chosen_size)
    runner.metadata[DESCRIPTION_METANAME] = current_experiment_name
    # run the perf benchmark for the function
    benchmark = runner.bench_func(
        "mcopies", bench_copy_function, copies.mcopies_ofc, chosen_size
    )
    # save the perf results from running the benchmark
    benchmark.dump(
        "results/" + current_experiment_name + ".json", compact=False, replace=True
    )
