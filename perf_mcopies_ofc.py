"""Benchmarks with perf for the functions in the copies module"""

import os
import sys
import perf

from tada.util import configuration

sys.path.insert(0, "/home/gkapfham/working/research/source/speed-surprises")
# pylint: disable=wrong-import-position
# pylint: disable=import-error
from speedsurprises.text import copies  # noqa: E402

DESCRIPTION_METANAME = "description"
PERF_EXPERIMENT_NAME = "perf_mcopies_ofc"


def run_benchmark(chosen_function, current_chosen_size):
    """Run a benchmark on a chosen_function and a current_chosen_size"""
    chosen_function(current_chosen_size)


def save_bencmark_results(current_benchmark):
    """Save the benchmark results to disk in a perf-formatted JSON file"""
    if not os.path.exists(configuration.RESULTS):
        os.makedirs(configuration.RESULTS)
    current_benchmark.dump(
        configuration.RESULTS
        + configuration.SEPARATOR
        + current_experiment_name
        + ".json",
        compact=False,
        replace=True,
    )


if __name__ == "__main__":
    # read the chosen_size
    filepath = configuration.CONFIGURATION
    with open(filepath) as fp:
        chosen_size = fp.readline().replace("\n", "")
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    current_experiment_name = PERF_EXPERIMENT_NAME + str(chosen_size)
    runner.metadata[DESCRIPTION_METANAME] = current_experiment_name
    # run the perf benchmark for the function
    benchmark = runner.bench_func(
        "mcopies", run_benchmark, copies.mcopies_ofc, chosen_size
    )
    # save the perf results from running the benchmark
    save_bencmark_results(benchmark)
