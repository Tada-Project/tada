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
    # expected_tuple = (generate.generate_int(current_size),)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data is not None


# pylint: disable=invalid-name
def test_generate_ints_makes_size_default():
    """Checks that requesting generated ints returns them"""
    # request a single tuple with an int in it
    requested_types = ["int", "int"]
    # assume the doubling experiment is at 100
    current_size = 100
    # the default generator will return a tuple with two 100 in it
    # expected_tuple = (generate.generate_int(current_size), generate.generate_int(current_size),)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data is not None


# pylint: disable=invalid-name
def test_generate_int_list__makes_size_default():
    """Checks that requesting generated ints returns them"""
    # request a single tuple with an int in it
    requested_types = ["int_list"]
    # assume the doubling experiment is at 100
    current_size = 100
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data is not None


# pylint: disable=invalid-name
def test_generate_char_list_makes_letter_default():
    """Checks that requesting a generated char returns one"""
    # request a single tuple with an int in it
    requested_types = ["char_list"]
    # assume the doubling experiment is at 100; not needed for this test
    current_size = 100
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data is not None


# pylint: disable=invalid-name
def test_generate_char_makes_letter_default():
    """Checks that requesting a generated char returns one"""
    # request a single tuple with a char in it
    requested_types = ["char"]
    # assume the doubling experiment is at 100; not needed for this test
    current_size = 100
    # the default generator will return a tuple with the default character in it
    expected_tuple = (generate.generate_char(current_size),)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


# pylint: disable=invalid-name
def test_generate_string_makes_string_default():
    """Checks that requesting a generated string returns one"""
    # request a single tuple with a string in it
    requested_types = ["string"]
    # assume the doubling experiment is at 100; not needed for this test
    current_size = 100
    # the default generator will return a tuple with the default string in it
    expected_tuple = (generate.generate_string(current_size),)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


# pylint: disable=invalid-name
def test_generate_boolean_makes_boolean_default():
    """Checks that requesting a generated bolean returns one"""
    # request a single tuple with an int in it
    requested_types = ["boolean"]
    # assume the doubling experiment is at 100; not needed for this test
    current_size = 100
    # the default generator will return a tuple with the default character in it
    expected_tuple = (generate.DEFAULT_VALUE_BOOLEAN,)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


def test_generate_float_makes_size_default():
    """Checks that requesting a generated float returns one"""
    # request a single tuple with an float in it
    requested_types = ["float"]
    # assume the doubling experiment is at 100
    current_size = 100
    # the default generator will return a tuple with 100 in it
    expected_tuple = (current_size,)
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data == expected_tuple


def test_generate_floats_makes_size_default():
    """Checks that requesting a generated float returns one"""
    # request a single tuple with an float in it
    requested_types = ["float", "float"]
    # assume the doubling experiment is at 100
    current_size = 100
    # generate the data for the requested_types and the current_size
    generated_data = generate.generate_data(requested_types, current_size)
    assert generated_data is not None


def test_generate_strategy_with_one_json(tmpdir):
    """Checks that generate strategy works for one json object in file"""
    # pylint: disable=blacklisted-name
    def foo(a):
        """A sample function"""
        type(a)

    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write('[{"type": "array", "items": {"type": "number"}}]')
    size = "50"
    function = generate.generate_strategy(foo, path, size)
    assert str(type(function)) == "<class 'function'>"


def test_generate_strategy_multiple_json(tmpdir):
    """Checks that generate strategy works for one json object in file"""
    # pylint: disable=blacklisted-name
    def foo(a):
        """A sample function"""
        type(a)

    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write(
        '[{"type": "array", "items": {"type": "number"}}\n\
        ,{"type": "array", "items": {"type": "number"}}]'
    )
    size = "50"
    function = generate.generate_strategy(foo, path, size)
    assert str(type(function)) == "<class 'function'>"
