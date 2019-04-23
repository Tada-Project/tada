"""Generate data for Tada"""

import sys
import random
import string

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
        # print("chosen_types", chosen_types)
        # print("chosen_size", chosen_size)
        # print("generated_values:", generated_values)
    return generated_values


def generate_int(chosen_size):
    """Generate an int value"""
    return int(chosen_size)


def generate_int_list(chosen_size):
    """Generate an int list"""
    output = [random.random() for _ in range(int(chosen_size))]
    # print(output)
    return output


# pylint: disable=unused-argument
def generate_char_list(chosen_size):
    """Generate a char list"""
    output = [random.choice(string.ascii_letters + string.digits) for _ in range(int(chosen_size))]
    # print(output)
    return output
