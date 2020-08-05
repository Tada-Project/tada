"""Run programs for Tada"""

import subprocess
from typing import Tuple

from pathlib import Path

path = Path(__file__).parent.parent.absolute()


def run_command(command: str) -> Tuple[bytes, bytes]:
    """Run a command and return the output and error code"""
    # Change working directory to the file's grandparent dir
    process = subprocess.Popen(
        command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, cwd=path,
    )
    output, error = process.communicate()
    return output, error


def run_benchmark(chosen_function, *args):
    """Run a benchmark on a chosen_function and a chosen size and *args"""
    return chosen_function(*args)
