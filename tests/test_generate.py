"""Tests for the generate module"""

from hypothesis_jsonschema import from_schema
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


def test_generate_data_with_hypothesis(tmpdir):
    """Checks that requesting a generated hypothesis data returns one"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write('[{"type": "array", "items": {"type": "integer"}}]')
    # assume the doubling experiment is at 100
    current_size = 100
    level = 1
    position = [0]
    requested_types = ["hypothesis"]
    requested_oath = str(path)
    generated_data = generate.generate_data(
        requested_types, current_size, level, position, requested_oath
    )
    assert generated_data is not None


def test_generate_function_with_one_json(tmpdir):
    """Checks that generate function works for one json object in file"""
    # pylint: disable=blacklisted-name
    def foo(a):
        """A sample function"""
        type(a)

    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write('[{"type": "array", "items": {"type": "number"}}]')
    size = "50"
    function = generate.generate_func(foo, path, size)
    assert str(type(function)) == "<class 'function'>"


def test_generate_function_multiple_json(tmpdir):
    """Checks that generate function works for two json objects in file"""
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
    function = generate.generate_func(foo, path, size)
    assert str(type(function)) == "<class 'function'>"


def test_generate_strategy_with_one_json(tmpdir):
    """Checks that generate strategy works for one json object in file"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write('[{"type": "array", "items": {"type": "number"}}]')
    size = "50"
    strategy = generate.generate_experiment_strategy(path, size)
    assert (
        str(strategy[0])
        == "lists(floats(allow_infinity=False, \
allow_nan=False).filter(lambda n: <unknown>), max_size=50, min_size=50)"
    )


def test_generate_strategy_multiple_json(tmpdir):
    """Checks that generate strategy works for two json objects in file"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write(
        '[{"type": "array", "items": {"type": "number"}}\n\
        ,{"type": "array", "items": {"type": "number"}}]'
    )
    size = "50"
    strategy = generate.generate_experiment_strategy(path, size)
    assert (
        str(strategy[0])
        == "lists(floats(allow_infinity=False, \
allow_nan=False).filter(lambda n: <unknown>), max_size=50, min_size=50)"
    )
    assert (
        str(strategy[1])
        != "lists(floats(allow_infinity=False, \
allow_nan=False).filter(lambda n: <unknown>), max_size=50, min_size=50)"
    )


def test_generate_strategy_multiple_json_2(tmpdir):
    """Checks that generate strategy works for two json objects in file"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write(
        '[{"type": "array", "items": {"type": "number"}}\n\
        ,{"type": "array", "items": {"type": "number"}}]'
    )
    size = "50"
    strategy = generate.generate_experiment_strategy(path, size)
    assert (
        str(strategy[1])
        != "lists(floats(allow_infinity=False, \
allow_nan=False).filter(lambda n: <unknown>), max_size=50, min_size=50)"
    )
    assert (
        str(strategy[0])
        == "lists(floats(allow_infinity=False, \
allow_nan=False).filter(lambda n: <unknown>), max_size=50, min_size=50)"
    )


def test_detect_level_and_position(tmpdir):
    """Checks that generate strategy works for multiple level"""
    path = tmpdir.mkdir('sub').join('hello.txt')
    path.write(
        '[{"type": "array", "items": [{"type": "number"}, {"type": "number"}]}\n\
        ,{"type": "array", "items": [{"type": "number"}, {"type": "number"}]}]'
    )
    size = '50'
    level = 2
    position = [0, 0]
    strategy = generate.generate_experiment_strategy(path, size, level,
                                                     position)
    assert (
        str(strategy[1])
        == 'builds(<function _operator.add>, tuples(floats(allow_infinity=False, allow_nan=False).filter(lambda n: <unknown>), floats(allow_infinity=False, allow_nan=False).filter(lambda n: <unknown>)).map(list), lists(recursive(one_of(one_of(one_of(one_of(none(), booleans()), integers()), floats(allow_infinity=False, allow_nan=False).map(lambda x: <unknown>)), text()), lambda strategy: st.lists(strategy, max_size=3), max_leaves=100)))'  # pylint: disable=C0301
    )


def test_generate_func_from_single_st():
    """Checks that generate function from single strategy works"""
    # pylint: disable=blacklisted-name
    def foo(a):
        """A sample function"""
        type(a)

    schema = {"type": "array", "items": {"type": "number"}}
    strategy = from_schema(schema)
    function = generate.generate_func_from_single_st(foo, strategy)
    assert str(type(function)) == "<class 'function'>"
