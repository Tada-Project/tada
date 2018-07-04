"""Tests for the arguments module"""

import pytest

# pylint: disable=import-error
from tada.util import arguments

VERIFIED = True
NOT_VERIFIED = False

EMPTY_STRING = ""
ERROR = "error:"
DIRECTORY = "--directory"


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
    "chosen_arguments",
    [
        (["--directory", "D"]),
        (["--directory", "d"]),
        (["--directory", "/a/"]),
        (["--directory", "/a/b/c/"]),
    ],
)
def test_directory_argument_verifiable(chosen_arguments):
    """Check that valid directory arguments will verify correctly"""
    parsed_arguments = arguments.parse(chosen_arguments)
    verified_arguments = arguments.verify(parsed_arguments)
    assert verified_arguments is True
