"""Generate data for Tada"""

import sys

GENERATE = sys.modules[__name__]

DEFAULT_VALUE_INT = 0
DEFAULT_VALUE_CHAR = "C"
DEFAULT_VALUE_TEXT = "TEXT"


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
    return int(chosen_size)
# pylint: disable=unused-argument
def generate_char(chosen_size):
    """Generate a char value"""
    return DEFAULT_VALUE_CHAR
# pylint: disable=unused-argument
def generate_float(chosen_size):
    """Generate an float value"""
    return float(chosen_size)
