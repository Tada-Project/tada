"""Configuration for Tada and perf"""

import json
import os

from typing import Any, Dict
from . import constants

WRITE = "w"

DIRECTORY = "directory"
FUNCTION = "function"
MODULE = "module"
DATADIRECTORY = "data_directory"
DATAFUNCTION = "data_function"
DATAMODULE = "data_module"
TYPES = "types"
SCHEMA = "schema"
LEVEL = "level"
SORTED = "sorted"
POSITION = "position"


def save(configuration_filename: str, tada_configuration: Dict[str, Any]) -> None:
    """Save the JSON file of the dictionary in configuration_file"""
    # Change working directory to the file's grandparent dir
    dirname = os.path.dirname
    os.chdir(dirname(dirname(__file__)))
    with open(configuration_filename, WRITE) as json_output_file:
        json.dump(tada_configuration, json_output_file)


def read(configuration_filename):
    """Read the JSON file of the dictionary in configuration_file"""
    # Change working directory to the file's grandparent dir
    dirname = os.path.dirname
    os.chdir(dirname(dirname(__file__)))
    with open(configuration_filename) as json_data_file:
        tada_configuration = json.load(json_data_file)
    return tada_configuration


def get_level(current_dictionary):
    """Return the level argument from the provided dictionary"""
    return current_dictionary[LEVEL]


def get_position(current_dictionary):
    """Return the position argument from the provided dictionary"""
    return current_dictionary[POSITION]


def get_sortinput(current_dictionary):
    """Return the sortinput argument from the provided dictionary"""
    return current_dictionary[SORTED]


def get_directory(current_dictionary):
    """Return the directory argument from the provided dictionary"""
    return current_dictionary[DIRECTORY]


def get_function(current_dictionary: Dict[str, Any]) -> str:
    """Return the function argument from the provided dictionary"""
    return current_dictionary[FUNCTION]


def get_module(current_dictionary: Dict[str, Any]) -> str:
    """Return the module argument from the provided dictionary"""
    return current_dictionary[MODULE]


def get_data_directory(current_dictionary):
    """Return the directory argument from the provided dictionary"""
    return current_dictionary[DATADIRECTORY]


def get_data_function(current_dictionary: Dict[str, Any]) -> str:
    """Return the function argument from the provided dictionary"""
    return current_dictionary[DATAFUNCTION]


def get_data_module(current_dictionary: Dict[str, Any]) -> str:
    """Return the module argument from the provided dictionary"""
    return current_dictionary[DATAMODULE]


def get_types(current_dictionary):
    """Return the types argument from the provided dictionary"""
    return current_dictionary[TYPES]


def get_schema_path(current_dictionary):
    """Return the schema path argument from the provided dictionary"""
    return current_dictionary[SCHEMA]


def get_experiment_name(current_dictionary: Dict[str, Any], chosen_size: int) -> str:
    """Return the complete name of an experiment"""
    return (
        constants.TADA
        + constants.UNDERSCORE
        + get_module(current_dictionary).replace(constants.PERIOD, constants.NONE)
        + constants.UNDERSCORE
        + get_function(current_dictionary).replace(constants.UNDERSCORE, constants.NONE)
        + constants.UNDERSCORE
        + str(chosen_size)
    )


def get_experiment_info(current_dictionary):
    """Return the complete name of an experiment"""
    return (
        constants.TADA
        + constants.UNDERSCORE
        + get_module(current_dictionary).replace(constants.PERIOD, constants.NONE)
        + constants.UNDERSCORE
        + get_function(current_dictionary).replace(constants.UNDERSCORE, constants.NONE)
    )
