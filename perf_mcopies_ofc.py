"""Benchmarks with perf for the functions in the copies module"""

import os
import sys
import perf

from tada.util import configuration
from tada.util import run
from tada.util import save

PERF_EXPERIMENT_NAME = "perf_mcopies_ofc"

if __name__ == "__main__":
    sys.path.insert(0, "/home/gkapfham/working/research/source/speed-surprises")
    # pylint: disable=import-error
    from speedsurprises.text import copies  # noqa: E402

    # read the chosen_size
    filepath = configuration.CONFIGURATION
    with open(filepath) as fp:
        chosen_size = fp.readline().replace("\n", "")
    # configure perf
    runner = perf.Runner()
    # configure the run of the benchmark
    current_experiment_name = PERF_EXPERIMENT_NAME + str(chosen_size)
    runner.metadata[configuration.DESCRIPTION_METANAME] = current_experiment_name
    # run the perf benchmark for the function
    current_benchmark = runner.bench_func(
        "mcopies", run.run_benchmark, copies.mcopies_ofc, chosen_size
    )
    # save the perf results from running the benchmark
    save.save_bencmark_results(current_benchmark, current_experiment_name)
