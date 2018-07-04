"""Read entities for Tada"""

# pylint: disable=relative-beyond-top-level
from . import configuration


def read_value(filepath):
    """Read the value from the filepath"""
    with open(filepath) as file_pointer:
        chosen_line = file_pointer.readline().replace("\n", "")
        return chosen_line


def read_experiment_size():
    """Read the experiment size from the configuration file"""
    filepath = configuration.CONFIGURATION
    return read_value(filepath)


def read_directory():
    """Read the directory from the configuration file"""
    filepath = configuration.DIRECTORY
    return read_value(filepath)
