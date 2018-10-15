"""Read entities for Tada"""

from . import constants


def read_value(filepath):
    """Read the value from the filepath"""
    with open(filepath) as file_pointer:
        chosen_line = file_pointer.readline().replace("\n", "")
        return chosen_line


def read_experiment_size():
    """Read the experiment size from the constants.file"""
    filepath = constants.SIZE
    return read_value(filepath)


def read_directory():
    """Read the directory from the constants.file"""
    filepath = constants.DIRECTORY
    return read_value(filepath)
