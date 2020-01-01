"""Tests for the configuration module"""

import pytest

from tada.util import arguments
from tada.util import configuration
from tada.util import constants


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (["--directory", "D", "--module", "M", "--function", "F", "--types", "T"]),
        (["--directory", "d", "--module", "m", "--function", "f", "--types", "t"]),
        (
            [
                "--directory",
                "/d/",
                "--module",
                "m.a",
                "--function",
                "fullname",
                "--types",
                "t",
            ]
        ),
        (
            [
                "--directory",
                "/a/b/c/",
                "--module",
                "m.a.a",
                "--function",
                "full_name",
                "--types",
                "char_list",
            ]
        ),
        (["--dir", "/a/", "--mod", "m", "--func", "f", "--types", "t"]),
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
        (["--directory", "D", "--module", "M", "--function", "F", "--types", "T"]),
        (["--directory", "d", "--module", "m", "--function", "f", "--types", "t"]),
        (
            [
                "--directory",
                "/d/",
                "--module",
                "m.a",
                "--function",
                "fullname",
                "--types",
                "type",
            ]
        ),
        (
            [
                "--directory",
                "/a/b/c/",
                "--module",
                "m.a.a",
                "--function",
                "full_name",
                "--types",
                "int_type",
            ]
        ),
        (["--dir", "/a/", "--mod", "m", "--func", "f", "--types", "t"]),
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


@pytest.mark.parametrize(
    "correct_arguments, correct_schema",
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
                "hypothesis",
                "--schema",
                "../schema.json",
            ],
            "../schema.json",
        )
    ],
)
# pylint: disable=invalid-name
def test_configuration_file_correct_schema_path(
        correct_arguments, correct_schema, tmpdir
):
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
    assert configuration.get_schema_path(tada_configuration_dict) == correct_schema


@pytest.mark.parametrize(
    "correct_arguments, correct_function, correct_module",
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
            "F",
            "M",
        )
    ],
)
# pylint: disable=invalid-name
# pylint: disable=bad-continuation
def test_configuration_file_correct_functions_modules(
    correct_arguments, correct_function, correct_module, tmpdir
):
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
    assert configuration.get_function(tada_configuration_dict) == correct_function
    assert configuration.get_module(tada_configuration_dict) == correct_module


@pytest.mark.parametrize(
    "correct_arguments, correct_experiment_name",
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
            "tada_M_F_2",
        )
    ],
)
# pylint: disable=invalid-name
# pylint: disable=bad-continuation
def test_configuration_file_correct_experiment_name(
    correct_arguments, correct_experiment_name, tmpdir
):
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
    assert (
        configuration.get_experiment_name(tada_configuration_dict, 2)
        == correct_experiment_name
    )


@pytest.mark.parametrize(
    "correct_arguments, correct_experiment_info",
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
            "tada_M_F",
        )
    ],
)
# pylint: disable=invalid-name
# pylint: disable=bad-continuation
def test_configuration_file_correct_experiment_info(
    correct_arguments, correct_experiment_name, tmpdir
):
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
    assert (
        configuration.get_experiment_info(tada_configuration_dict)
        == correct_experiment_info
    )
