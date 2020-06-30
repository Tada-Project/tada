"""Tests for the arguments module"""

import pytest

from tada.util import arguments

VERIFIED = True
NOT_VERIFIED = False

EMPTY_STRING = ""
ERROR = "error:"
DIRECTORY = "--directory"
MODULE = "--module"
FUNCTION = "--function"


@pytest.fixture
def no_arguments():
    """Return no command-line arguments"""
    return []


# pylint: disable=invalid-name
# pylint: disable=redefined-outer-name
def test_default_argument_values_incorrect(no_arguments, capsys):
    """No command-line arguments is incorrect"""
    with pytest.raises(SystemExit):
        arguments.parse(no_arguments)
    standard_out, standard_err = capsys.readouterr()
    assert standard_out is EMPTY_STRING
    assert ERROR in standard_err
    assert DIRECTORY in standard_err


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (
            [
                "--directory",
                "d",
                "--module",
                "m",
                "--function",
                "f",
                "--types",
                "t",
            ]
        ),
        (
            [
                "--directory",
                "D",
                "--module",
                "M",
                "--function",
                "F",
                "--types",
                "T",
            ]
        ),
        (
            [
                "--directory",
                "/d/",
                "--module",
                "m.a",
                "--function",
                "fullname",
                "--types",
                "int",
            ]
        ),
        (
            [
                "--directory",
                "/a/b/c/",
                "--module",
                "m.a.a",
                "--function",
                "full.name",
                "--types",
                "int_list",
            ]
        ),
        (["--dir", "/a/", "--mod", "m", "--func", "f", "--types", "t"]),
    ],
)
def test_directory_argument_verifiable(correct_arguments):
    """Check that valid directory arguments will verify correctly"""
    parsed_arguments = arguments.parse(correct_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is True


@pytest.mark.parametrize(
    "chosen_arguments",
    [(["--module", "", "--directory", "", "--function", "", "--types", ""])],
)
def test_module_argument_not_verifiable(chosen_arguments):
    """Check that not valid directory arguments will not verify correctly"""
    parsed_arguments = arguments.parse(chosen_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is False


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (
            [
                "--module",
                "",
                "--directory",
                "/d/",
                "--function",
                "f",
                "--types",
                "t",
            ]
        )
    ],
)
def test_only_module_argument_not_verifiable(chosen_arguments):
    """Check that not valid directory arguments will not verify correctly"""
    parsed_arguments = arguments.parse(chosen_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is False


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (
            [
                "--module",
                "m",
                "--directory",
                "/d/",
                "--function",
                "",
                "--types",
                "t",
            ]
        )
    ],
)
def test_only_function_argument_not_verifiable(chosen_arguments):
    """Check that not valid directory arguments will not verify correctly"""
    parsed_arguments = arguments.parse(chosen_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is False


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (
            [
                "--module",
                "m",
                "--directory",
                "/d/",
                "--function",
                "f",
                "--types",
                "",
            ]
        )
    ],
)
def test_only_type_argument_not_verifiable(chosen_arguments):
    """Check that not valid directory arguments will not verify correctly"""
    parsed_arguments = arguments.parse(chosen_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is False


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (["--directories", "d"]),
        (["--dirs", "d"]),
        (["--directoryy", "d"]),
        (["--ddirectory", "d"]),
        (["-directory", "d"]),
    ],
)
def test_directory_argument_not_verifiable_syserror(chosen_arguments, capsys):
    """Check that not valid directory arguments will not verify correctly"""
    with pytest.raises(SystemExit):
        arguments.parse(chosen_arguments)
    standard_out, standard_err = capsys.readouterr()
    assert standard_out is EMPTY_STRING
    assert ERROR in standard_err
    assert DIRECTORY in standard_err


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (["--modules", "m"]),
        (["--mods", "m"]),
        (["--modulle", "m"]),
        (["--mmodule", "m"]),
        (["-module", "m"]),
    ],
)
def test_module_argument_not_verifiable_syserror(chosen_arguments, capsys):
    """Check that not valid module arguments will not verify correctly"""
    with pytest.raises(SystemExit):
        arguments.parse(chosen_arguments)
    standard_out, standard_err = capsys.readouterr()
    assert standard_out is EMPTY_STRING
    assert ERROR in standard_err
    assert MODULE in standard_err


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (["--functions", "f"]),
        (["--funcs", "f"]),
        (["--functtion", "f"]),
        (["--ffunction", "f"]),
        (["-function", "f"]),
    ],
)
def test_function_argument_not_verifiable_syserror(chosen_arguments, capsys):
    """Check that not valid function arguments will not verify correctly"""
    with pytest.raises(SystemExit):
        arguments.parse(chosen_arguments)
    standard_out, standard_err = capsys.readouterr()
    assert standard_out is EMPTY_STRING
    assert ERROR in standard_err
    assert MODULE in standard_err


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (
            [
                "--directory",
                "/d/", "/a/",
                "--module",
                "m.a",
                "--function",
                "fullname",
                "--types",
                "int",
            ]
        ),
        (
            [
                "--directory",
                "/a/b/c/", "/d/e/f",
                "--module",
                "m.a.a",
                "--function",
                "full.name",
                "--types",
                "int_list",
            ]
        ),
        (["--dir", "/a/", "/b/", "--mod", "m", "--func", "f", "--types", "t"]),
        (
            [
                "--directory",
                "/a/b/c/", "/d/e/f",
                "--module",
                "m.a.a", "m.a.b",
                "--function",
                "full.name",
                "--types",
                "int_list",
            ]
        ),
        (["--dir", "/a/", "/b/", "--mod", "m", "n", "--func", "f", "--types", "t"]),
        (
            [
                "--directory",
                "/a/b/c/",
                "--module",
                "m.a.a", "m.a.b",
                "--function",
                "full.name",
                "--types",
                "int_list",
            ]
        ),
        (["--dir", "/a/", "--mod", "m", "n", "--func", "f", "--types", "t"]),
        (["--dir", "/a/", "--mod", "m", "--func", "f", "g", "--types", "t"]),
        (
            [
                "--directory",
                "/a/b/c/",
                "--module",
                "m.a.a m.a.b",
                "--function",
                "full.name1", "full.name2",
                "--types",
                "int_list",
            ]
        ),
        (["--dir", "/a/", "--mod", "m n", "--func", "f", "g", "--types", "t"]),
    ],
)
def test_two_sets_arguments(correct_arguments):
    """Check that valid directory arguments will verify correctly"""
    parsed_arguments = arguments.parse_args(correct_arguments)
    verified_first = arguments.verify(parsed_arguments[0])
    verified_second = arguments.verify(parsed_arguments[1])
    assert verified_first is True
    assert verified_second is True
