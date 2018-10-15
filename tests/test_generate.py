"""Tests for the generate module"""

from tada.util import generate


# pylint: disable=invalid-name
def test_generate_int_makes_size_default():
    """Checks that requesting a generated int returns one"""
    # request a single tuple with an int in it
    requested_types = ["int"]
    # assume the doubling experiment is at 100
    current_size = 100
    # the default generator will return a tuple with 100 in it
    expected_tuple = (current_size,)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


# pylint: disable=invalid-name
def test_generate_ints_makes_size_default():
    """Checks that requesting generated ints returns them"""
    # request a single tuple with an int in it
    requested_types = ["int", "int"]
    # assume the doubling experiment is at 100
    current_size = 100
    # the default generator will return a tuple with two 100 in it
    expected_tuple = (current_size, current_size,)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


# pylint: disable=invalid-name
def test_generate_char_makes_letter_default():
    """Checks that requesting a generated char returns one"""
    # request a single tuple with an int in it
    requested_types = ["char"]
    # assume the doubling experiment is at 100; not needed for this test
    current_size = 100
    # the default generator will return a tuple with the default character in it
    expected_tuple = (generate.DEFAULT_VALUE_CHAR,)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple
