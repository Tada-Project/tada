"""Run programs for Tada"""

import subprocess


def run_command(command):
    """Run a command and return the output and error code"""
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True
    )
    output, error = process.communicate()
    return output, error


def run_benchmark(chosen_function, *args):
    """Run a benchmark on a chosen_function and a chosen size and *args"""
    return chosen_function(*args)
