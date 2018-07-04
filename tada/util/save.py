"""Run entities for Tada"""

import os

# pylint: disable=relative-beyond-top-level
from . import configuration


def save_configuration(configurationfile, current_size):
    """Save the current size configuration for the experiment to a file"""
    with open(configurationfile, "w") as file_pointer:
        file_pointer.write(str(current_size))


def save_bencmark_results(current_benchmark, current_experiment_name):
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
