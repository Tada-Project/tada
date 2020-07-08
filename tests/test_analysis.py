"""Tests for the analysis module"""

import pytest

from tada.util import analysis


@pytest.mark.parametrize(
    "chosen_result",
    [0, 2, 4, 8, 15],
)
def test_analyze_big_oh(chosen_result):
    """Checks big_oh is correctly analyzed"""
    output = analysis.analyze_big_oh(chosen_result)
    assert output is not None
