"""Generate data for Tada"""

import json
import sys
import random
import string
from hypothesis_jsonschema import from_schema

GENERATE = sys.modules[__name__]

DEFAULT_VALUE_INT = random.randint(0, 100)
DEFAULT_VALUE_CHAR = "C"
DEFAULT_VALUE_TEXT = "TEXT"
DEFAULT_VALUE_BOOLEAN = True


def generate_strategy(json_path):
    """Generate a hypothesis strategy from the given jsonschema"""
    with open(json_path) as json_file:
        json_dict = json.load(json_file)
        strategy = from_schema(json_dict)
    return strategy


def generate_data(chosen_types, chosen_size):
    """Generate a list of data values"""
    generated_values = ()
    # call a generate function for each type
    for current_type in chosen_types:
        generator_to_invoke = getattr(GENERATE, "generate_" + str(current_type))
        generated_value = generator_to_invoke(chosen_size)
        generated_values = generated_values + (generated_value,)
    return generated_values


# pylint: disable=unused-argument
def generate_int(chosen_size):
    """Generate an int value"""
    lowerbound = 10**(int(chosen_size) - 1)
    upperbound = (10**int(chosen_size)) - 1
    return random.randint(lowerbound, upperbound)
    # return 10**(int(chosen_size))


def generate_int_list(chosen_size):
    """Generate an int list"""
    output = [random.random() for _ in range(int(chosen_size))]
    return output


def generate_char_list(chosen_size):
    """Generate a char list"""
    output = [random.choice(string.ascii_letters + string.digits) for _ in range(int(chosen_size))]
    return output


# pylint: disable=unused-argument
def generate_char(chosen_size):
    """Generate a char value"""
    return DEFAULT_VALUE_CHAR


# pylint: disable=unused-argument
def generate_string(chosen_size):
    """Generate a string value"""
    return DEFAULT_VALUE_TEXT


# pylint: disable=unused-argument
def generate_boolean(chosen_size):
    """Generate a boolean value"""
    return DEFAULT_VALUE_BOOLEAN


def generate_float(chosen_size):
    """Generate an float value"""
    return float(chosen_size)
