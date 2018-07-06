"""Generate data for Tada"""

import sys

GENERATE = sys.modules[__name__]

DEFAULT_VALUE_INT = 0
DEFAULT_VALUE_TEXT = "C"


def generate_data(chosen_types, chosen_size):
    """Generate a list of data values"""
    generated_values = ()
    # call a generate function for each type
    for current_type in chosen_types:
        generator_to_invoke = getattr(GENERATE, "generate_" + str(current_type))
        generator_to_invoke(chosen_size)
    return generated_values


def generate_int(chosen_size):
    """Generate an int value"""
    return chosen_size
