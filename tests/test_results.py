"""Tests for the results module"""

from prettytable import PrettyTable
from tada.util import results

resultstable = PrettyTable(['Size', 'Mean', 'Median', 'Ratio'])


def test_add_resultstable():
    """Add one to each column to test resultstable change"""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    assert resultstable1 is not resultstable
