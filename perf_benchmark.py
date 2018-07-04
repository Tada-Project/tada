"""Benchmarks with perf for the function under analysis"""

import importlib
import perf

from tada.util import constants
from tada.util import run
from tada.util import package
from tada.util import read
from tada.util import save

if __name__ == "__main__":
    # TODO: Generalize these to work for values read from configuration
    chosen_directory = read.read_directory()
    package.add_sys_path(chosen_directory)
    module = importlib.import_module("speedsurprises.text.copies")
    method = getattr(module, "mcopies_ofc")

    # read the chosen_size
    chosen_size = read.read_experiment_size()
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    # TODO: Make this based on the name of the experiment
    current_experiment_name = constants.PERF_BENCHMARK + str(chosen_size)
    runner.metadata[constants.DESCRIPTION_METANAME] = current_experiment_name
    # TODO: Make this run the function read from the configuration
    current_benchmark = runner.bench_func(
        "mcopies", run.run_benchmark, method, chosen_size
    )
    # save the perf results from running the benchmark
    save.save_bencmark_results(current_benchmark, current_experiment_name)
