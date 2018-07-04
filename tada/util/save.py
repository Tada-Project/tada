"""Save entities for Tada"""

import os

# pylint: disable=relative-beyond-top-level
from . import configuration


def save_experiment_size(configuration_file, current_size):
    """Save the current size configuration for the experiment to a file"""
    with open(configuration_file, "w") as file_pointer:
        file_pointer.write(str(current_size))


def save_directory(directory_file, directory_name):
    """Save the current directory for the analyzed functions to a file"""
    with open(directory_file, "w") as file_pointer:
        file_pointer.write(directory_name)


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
