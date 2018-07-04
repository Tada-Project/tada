"""Configuration for Tada and perf"""

import json

WRITE = 'w'

DIRECTORY = "directory"


def save(configuration_filename, tada_configuration):
    """Save the JSON file of the dictionary in configuration_file"""
    with open(configuration_filename, WRITE) as json_output_file:
        json.dump(tada_configuration, json_output_file)


def read(configuration_filename):
    """Read the JSON file of the dictionary in configuration_file"""
    with open(configuration_filename) as json_data_file:
        tada_configuration = json.load(json_data_file)
    return tada_configuration
