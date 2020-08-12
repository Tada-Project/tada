"""Generate data for Tada"""

import sys
import random
import string
from hypothesis_jsonschema import from_schema
from hypothesis import given, settings
from hypothesis import HealthCheck
from . import read


GENERATE = sys.modules[__name__]

DEFAULT_VALUE_INT = random.randint(0, 100)
DEFAULT_VALUE_CHAR = "C"
DEFAULT_VALUE_TEXT = "TEXT"
DEFAULT_VALUE_BOOLEAN = True

TYPES = [
    "int",
    "int_list",
    "char",
    "char_list",
    "boolean",
    "string",
    "float",
    "bitdepth",
]

# initialize data as tuple
global_data = ()


# pylint: disable=W0102
def store_data_to_global(path, chosen_size, level=1, position=[0]):
    """Generate data through global variable"""

    def store_global(a):
        """A dummy function to store the data to file for experiment"""
        # pylint: disable=global-statement
        global global_data
        global_data = global_data + (a,)

    strategies = generate_experiment_strategy(
        path, chosen_size, level, position
    )
    # store data based on the amount of parameters
    for st in strategies:
        gen = generate_func_from_single_st(store_global, st)
        gen()
    return global_data


def generate_experiment_strategy(
        path, size, level=1, position=[0]
):  # pylint: disable=W0102
    """generate strategies from a schema path and current input size"""
    json_schema = read.read_schema(path)

    # pylint: disable=W0102, R1705
    def detect_level_and_position(
            schema, level=1, position=[0], index_position=0
    ):
        """A dummy function to store the data to file for experiment"""
        if level == 0:
            return schema
        else:
            if isinstance(schema, list):
                subschema = schema[position[index_position]]
            elif isinstance(schema["items"], dict):
                subschema = schema["items"]
            elif isinstance(schema["items"], list):
                subschema = schema["items"][position[index_position]]
            return detect_level_and_position(
                subschema, level - 1, position, index_position + 1
            )

    js = detect_level_and_position(json_schema, level, position)
    double_experiment_size(js, size)
    strategy = []
    for j in json_schema:
        strategy.append(from_schema(j))
    return strategy


def double_experiment_size(schema, size):
    """modify the input data size for doubling experiment"""
    if schema.get("type") == "array":
        schema["maxItems"] = int(size)
        schema["minItems"] = int(size)
    elif schema.get("type") == "object":
        schema["maxProperties"] = int(size)
        schema["minProperties"] = int(size)
    elif schema.get("type") == "string":
        schema["maxLength"] = int(size)
        schema["minLength"] = int(size)
    else:
        schema["maximum"] = int(size)
        schema["minimum"] = int(size)


# pylint: disable=W0102
def generate_func(function, path, size, level=1, position=[0]):
    """generate a function with strategy from schema path and current input size"""
    strategy = generate_experiment_strategy(path, size, level, position)
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


# pylint: disable=W0102, R0913
def generate_data(
        chosen_types, chosen_size, level=1, position=[0], path=None, gen_func=None
):
    """Generate a list of data values"""
    generated_values = ()
    if chosen_types[0] in TYPES:
        # call a generate function for each type
        for current_type in chosen_types:
            generator_to_invoke = getattr(
                GENERATE, "generate_" + str(current_type)
            )
            generated_value = generator_to_invoke(chosen_size)
            generated_values = generated_values + (generated_value,)
    elif chosen_types[0] == "hypothesis":
        generated_values = store_data_to_global(
            path, chosen_size, level, position
        )
    elif chosen_types[0] == "custom":
        generated_values = gen_func(chosen_size)
    return generated_values


def generate_int(chosen_size):
    """Generate an int value"""
    return int(chosen_size)
    # return 10**(int(chosen_size))


def generate_bitdepth(chosen_size):
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
