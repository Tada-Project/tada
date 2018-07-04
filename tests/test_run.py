"""Tests for the run module"""

# pylint: disable=import-error
from tada.util import run


def test_run_command_returns_echo():
    """Checks that a single line is returned from command """
    output, error = run.run_command("echo \"Hello!\"")
    assert error == b''
    assert output == b'Hello!\n'
