"""Benchmarks with perf for the functions in the copies module"""

import importlib
import perf

from tada.util import constants
from tada.util import run
from tada.util import package
from tada.util import read
from tada.util import save

PERF_EXPERIMENT_NAME = "perf_mcopies_ofc"

if __name__ == "__main__":
    chosen_directory = read.read_directory()
    package.add_sys_path(chosen_directory)
    module = importlib.import_module("speedsurprises.text.copies")
    method = getattr(module, "mcopies_ofc")
    # from speedsurprises.text import copies  # noqa: E402
    # from m1 import copies  # noqa: E402

    # read the chosen_size
    chosen_size = read.read_experiment_size()
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    current_experiment_name = PERF_EXPERIMENT_NAME + str(chosen_size)
    runner.metadata[constants.DESCRIPTION_METANAME] = current_experiment_name
    # run the perf benchmark for the function
    # current_benchmark = runner.bench_func(
    #     "mcopies", run.run_benchmark, copies.mcopies_ofc, chosen_size
    # )
    current_benchmark = runner.bench_func(
        "mcopies", run.run_benchmark, method, chosen_size
    )

    # save the perf results from running the benchmark
    save.save_bencmark_results(current_benchmark, current_experiment_name)
