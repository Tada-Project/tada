"""Generate data for Tada"""

import sys
import random
import string
from hypothesis_jsonschema import from_schema
from hypothesis import given, settings
from hypothesis import HealthCheck
from . import constants
from . import read


GENERATE = sys.modules[__name__]

DEFAULT_VALUE_INT = random.randint(0, 100)
DEFAULT_VALUE_CHAR = "C"
DEFAULT_VALUE_TEXT = "TEXT"
DEFAULT_VALUE_BOOLEAN = True

TYPES = ["int", "int_list", "char", "char_list", "boolean", "string", "float"]

# initialize data as tuple
global_data = ()


def store_data_to_global(path, chosen_size):
    """Generate data through global variable"""

    def store_global(a):
        """A dummy function to store the data to file for experiment"""
        # pylint: disable=global-statement
        global global_data
        global_data = global_data + (a,)

    strategies = generate_experiment_strategy(path, chosen_size)
    # store data based on the amount of parameters
    for st in strategies:
        gen = generate_func_from_single_st(store_global, st)
        gen()
    return global_data


def store_data_to_file(a):
    """A dummy function to store the data to file for experiment """
    with open("data.txt", "w+") as f:
        f.write(str(a))


def generate_experiment_strategy(path, size):
    """generate strategies from a schema path and current input size"""
    json_schema = read.read_schema(path)
    # change the size as the experiment doubles
    for schema in json_schema:
        schema["maxItems"] = int(size)
        schema["minItems"] = int(size)
    strategy = []
    for j in json_schema:
        strategy.append(from_schema(j))
    return strategy


def generate_func(function, path, size):
    """generate a function with strategy from schema path and current input size"""
    strategy = generate_experiment_strategy(path, size)
    function = given(*strategy)(function)
    # configure hypothesis
    function = settings(
        max_examples=1,
        suppress_health_check=[
            HealthCheck.large_base_example,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
            HealthCheck.filter_too_much,
        ],
    )(function)
    return function


def generate_func_from_single_st(function, strategy):
    """generate function from a single strategy"""
    function = given(strategy)(function)
    # configure hypothesis
    function = settings(
        max_examples=1,
        suppress_health_check=[
            HealthCheck.large_base_example,
            HealthCheck.too_slow,
            HealthCheck.data_too_large,
            HealthCheck.filter_too_much,
        ],
    )(function)
    return function


def generate_data(chosen_types, chosen_size, path=None):
    """Generate a list of data values"""
    generated_values = ()
    if chosen_types[0] in TYPES:
        # call a generate function for each type
        for current_type in chosen_types:
            generator_to_invoke = getattr(GENERATE, "generate_" + str(current_type))
            generated_value = generator_to_invoke(chosen_size)
            generated_values = generated_values + (generated_value,)
    elif chosen_types[0] == "hypothesis":
        generated_values = store_data_to_global(path, chosen_size)
        if constants.SORT == 1:
            print("gotit")
            generated_values.sort()
    return generated_values


def generate_int(chosen_size):
    """Generate an int value"""
    lowerbound = 10 ** (int(chosen_size) - 1)
    upperbound = (10 ** int(chosen_size)) - 1
    return random.randint(lowerbound, upperbound)
    # return 10**(int(chosen_size))


def generate_int_list(chosen_size):
    """Generate an int list"""
    output = [random.random() for _ in range(int(chosen_size))]
    return output


def generate_char_list(chosen_size):
    """Generate a char list"""
    output = [
        random.choice(string.ascii_letters + string.digits)
        for _ in range(int(chosen_size))
    ]
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
