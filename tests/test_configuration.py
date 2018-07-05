"""Tests for the configuration module"""

import pytest

# pylint: disable=import-error
from tada.util import arguments
from tada.util import configuration
from tada.util import constants


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (["--directory", "D"]),
        (["--directory", "d"]),
        (["--directory", "/a/"]),
        (["--directory", "/a/b/c/"]),
        (["--dir", "/a/"]),
    ],
)
def test_configuration_file_saved(chosen_arguments, tmpdir):
    """Checks that the configuration file was saved to the directory"""
    parsed_arguments = arguments.parse(chosen_arguments)
    configuration.save(
        str(tmpdir) + "/" + constants.CONFIGURATION, vars(parsed_arguments)
    )
    assert len(tmpdir.listdir()) == 1


@pytest.mark.parametrize(
    "chosen_arguments",
    [
        (["--directory", "D"]),
        (["--directory", "d"]),
        (["--directory", "/a/"]),
        (["--directory", "/a/b/c/"]),
        (["--dir", "/a/"]),
    ],
)
# pylint: disable=invalid-name
def test_configuration_file_saved_retrieved(chosen_arguments, tmpdir):
    """Checks that the configuration file was saved to the directory"""
    parsed_arguments = arguments.parse(chosen_arguments)
    directory_prefix = str(tmpdir) + "/"
    configuration.save(
        directory_prefix + constants.CONFIGURATION, vars(parsed_arguments)
    )
    assert len(tmpdir.listdir()) == 1
    tada_configuration_dict = configuration.read(directory_prefix + constants.CONFIGURATION)
    assert tada_configuration_dict[configuration.DIRECTORY] == chosen_arguments[1]
    assert configuration.get_directory(tada_configuration_dict) == chosen_arguments[1]
