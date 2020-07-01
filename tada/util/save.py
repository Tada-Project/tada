"""Save entities for Tada"""

import os

from . import constants


def save_experiment_size(configuration_file: str, current_size: int) -> None:
    """Save the current size constants.for the experiment to a file"""
    with open(configuration_file, "w") as file_pointer:
        file_pointer.write(str(current_size))


def save_directory(directory_file: str, directory_name: str) -> None:
    """Save the current directory for the analyzed functions to a file"""
    with open(directory_file, "w") as file_pointer:
        file_pointer.write(directory_name)


def save_benchmark_results(current_benchmark, current_experiment_name):
    """Save the benchmark results to disk in a perf-formatted JSON file"""
    if not os.path.exists(constants.RESULTS):
        os.makedirs(constants.RESULTS)
    current_benchmark.dump(
        constants.RESULTS + constants.SEPARATOR + current_experiment_name + ".json",
        compact=False,
        replace=True,
    )
