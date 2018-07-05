"""Tests for the configuration module"""

import pytest

# pylint: disable=import-error
from tada.util import arguments
from tada.util import configuration
from tada.util import constants


@pytest.mark.parametrize(
    "correct_arguments",
    [
        (["--directory", "D", "--module", "M"]),
        (["--directory", "d", "--module", "m"]),
        (["--directory", "/d/", "--module", "m.a"]),
        (["--directory", "/a/b/c/", "--module", "m.a.a"]),
        (["--dir", "/a/", "--mod", "m"]),
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
        (["--directory", "D", "--module", "M"]),
        (["--directory", "d", "--module", "m"]),
        (["--directory", "/d/", "--module", "m.a"]),
        (["--directory", "/a/b/c/", "--module", "m.a.a"]),
        (["--dir", "/a/", "--mod", "m"]),
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
    tada_configuration_dict = configuration.read(directory_prefix + constants.CONFIGURATION)
    assert tada_configuration_dict[configuration.DIRECTORY] == correct_arguments[1]
    assert configuration.get_directory(tada_configuration_dict) == correct_arguments[1]
