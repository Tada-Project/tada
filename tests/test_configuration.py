"""Tests for the configuration module"""

import pytest

# pylint: disable=import-error
from tada.util import arguments
from tada.util import configuration
from tada.util import constants


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (["--directory", "D", "--module", "M", "--function", "F"]),
        (["--directory", "d", "--module", "m", "--function", "f"]),
        (["--directory", "/d/", "--module", "m.a", "--function", "fullname"]),
        (["--directory", "/a/b/c/", "--module", "m.a.a", "--function", "full_name"]),
        (["--dir", "/a/", "--mod", "m", "--func", "f"]),
    ],
)
def test_configuration_file_saved(correct_arguments, tmpdir):
    """Checks that the configuration file was saved to the directory"""
    parsed_arguments = arguments.parse(correct_arguments)
    configuration.save(
        str(tmpdir) + "/" + constants.CONFIGURATION, vars(parsed_arguments)
    )
    assert len(tmpdir.listdir()) == 1


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (["--directory", "D", "--module", "M", "--function", "F"]),
        (["--directory", "d", "--module", "m", "--function", "f"]),
        (["--directory", "/d/", "--module", "m.a", "--function", "fullname"]),
        (["--directory", "/a/b/c/", "--module", "m.a.a", "--function", "full_name"]),
        (["--dir", "/a/", "--mod", "m", "--func", "f"]),
    ],
)
# pylint: disable=invalid-name
def test_configuration_file_saved_retrieved(correct_arguments, tmpdir):
    """Checks that the configuration file was saved to the directory"""
    parsed_arguments = arguments.parse(correct_arguments)
    directory_prefix = str(tmpdir) + "/"
    configuration.save(
        directory_prefix + constants.CONFIGURATION, vars(parsed_arguments)
    )
    assert len(tmpdir.listdir()) == 1
    tada_configuration_dict = configuration.read(
        directory_prefix + constants.CONFIGURATION
    )
    assert tada_configuration_dict[configuration.DIRECTORY] == correct_arguments[1]
    assert configuration.get_directory(tada_configuration_dict) == correct_arguments[1]


@pytest.mark.parametrize(
    "correct_arguments, correct_types",
    [
        (
            [
                "--directory",
                "D",
                "--module",
                "M",
                "--function",
                "F",
                "--types",
                "int",
                "float",
                "text",
            ],
            ["int", "float", "text"],
        )
    ],
)
# pylint: disable=invalid-name
def test_configuration_file_correct_types(correct_arguments, correct_types, tmpdir):
    """Checks that the configuration file was saved to the directory"""
    parsed_arguments = arguments.parse(correct_arguments)
    directory_prefix = str(tmpdir) + "/"
    configuration.save(
        directory_prefix + constants.CONFIGURATION, vars(parsed_arguments)
    )
    assert len(tmpdir.listdir()) == 1
    tada_configuration_dict = configuration.read(
        directory_prefix + constants.CONFIGURATION
    )
    assert configuration.get_types(tada_configuration_dict) == correct_types
