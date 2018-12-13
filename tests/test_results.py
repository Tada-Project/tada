"""Tests for the results module"""

from tada.util import results
from prettytable import PrettyTable

resultstable = PrettyTable(['Size', 'Mean', 'Median', 'Ratio'])


def test_add_resultstable():
    resultstable1 = resultstable
    add_resultstable(resultstable1, 1, 1, 1, 1)
    assert resultstable1 is not resultstable
