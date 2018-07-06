"""Tests for the generate module"""

# pylint: disable=import-error
from tada.util import generate


# pylint: disable=invalid-name
def test_generate_int_makes_size_default():
    """Checks that requesting a generated int returns one"""
    requested_types = ["int"]
    current_size = 100
    generate.generate_data(requested_types, current_size)
