"""Configuration for Tada and perf"""

import json

WRITE = "w"

DIRECTORY = "directory"
FUNCTION = "function"
MODULE = "module"


def save(configuration_filename, tada_configuration):
    """Save the JSON file of the dictionary in configuration_file"""
    with open(configuration_filename, WRITE) as json_output_file:
        json.dump(tada_configuration, json_output_file)


def read(configuration_filename):
    """Read the JSON file of the dictionary in configuration_file"""
    with open(configuration_filename) as json_data_file:
        tada_configuration = json.load(json_data_file)
    return tada_configuration


def get_directory(current_dictionary):
    """Return the directory argument from the provided dictionary"""
    return current_dictionary[DIRECTORY]


def get_function(current_dictionary):
    """Return the function argument from the provided dictionary"""
    return current_dictionary[FUNCTION]


def get_module(current_dictionary):
    """Return the module argument from the provided dictionary"""
    return current_dictionary[MODULE]
