"""Tests for the results module"""

from prettytable import PrettyTable
from tada.util import results

resultstable = PrettyTable(['Size', 'Mean', 'Median', 'Ratio'])
data = resultstable.get_string()


def test_add_resultstable():
    """Add one to each column to test resultstable change"""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    data1 = resultstable1.get_string()
    assert data1 is not data


def test_add_resultstable_value():
    """Test the values inside of resultstable are what we want"""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    for row in resultstable1:
        row.border = False
        row.header = False
        data2 = row.get_string(fields=["Size"]).strip()
        data3 = row.get_string(fields=["Mean"]).strip()
        data4 = row.get_string(fields=["Median"]).strip()
        data5 = row.get_string(fields=["Ratio"]).strip()
    assertEqual(data2, "1")
    assertEqual(data3, "1")
    assertEqual(data4, "1")
    assertEqual(data5, "1")
