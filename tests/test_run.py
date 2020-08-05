"""Tests for the run module"""

from tada.util import run


def test_run_command_returns_echo():
    """Checks that a single line is returned from command"""
    output, error = run.run_command('echo \"Hello!\"')
    assert error == b""
    assert output is not None


# pylint: disable=invalid-name
def test_run_benchmark_provided_function():
    """Checks that chosen built-in sum function is run correctly"""
    chosen_function = sum
    chosen_arguments = [1, 2, 3]
    expected_sum_output = 6
    run_output = run.run_benchmark(chosen_function, chosen_arguments)
    assert run_output == expected_sum_output
