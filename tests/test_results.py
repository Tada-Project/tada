"""Tests for the resultstable and results module."""

from prettytable import PrettyTable
from tada.util import results

resultstable = PrettyTable(["Size", "Mean", "Median", "Ratio"])
data = resultstable.get_string()


def test_add_resultstable():
    """Add 1 to each column to test resultstable change."""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    data1 = resultstable1.get_string()
    assert data1 is not data


def test_add_resultstable_value():
    """Test adding items to results table and check value correctness."""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    for row in resultstable1:
        row.border = False
        row.header = False
        data2 = row.get_string(fields=["Size"]).strip()
        data3 = row.get_string(fields=["Mean"]).strip()
        data4 = row.get_string(fields=["Median"]).strip()
        data5 = row.get_string(fields=["Ratio"]).strip()
    assert data2 == "1"
    assert data3 == "1"
    assert data4 == "1"
    assert data5 == "1"


def test_display_resultstable():
    """Test to see if display_resulstable functions properly."""
    resultstable1 = resultstable
    results.add_resultstable(resultstable1, 1, 1, 1, 1)
    assert results.display_resultstable(resultstable1) != " "


def test_to_markdown_table():
    """Test to see if to_markdown_table functions properly."""
    results_table = PrettyTable(["Size", "Mean", "Median", "Ratio"])
    output = results.to_markdown_table(results_table)
    expect = (
        """ Size | Mean | Median | Ratio \n------|------|--------|-------"""
    )
    assert expect == output


def test_display_resultstable_to_markdown(capsys):
    """Test to see if display_resulstable functions properly when to_md is true."""
    results_table = PrettyTable(["Size", "Mean", "Median", "Ratio"])
    results.add_resultstable(results_table, 1, 1, 1, 1)
    results.display_resultstable(results_table, to_md=True)
    captured = capsys.readouterr()
    expect = """ Size | Mean | Median | Ratio \n\
------|------|--------|-------\n\
  1   |  1   |   1    |   1   \n"""
    assert captured.out == expect


def test_greatest_common_size():
    """Test if can find the greatest common size of two experiments"""
    input_data = {
        "insertion_sort": {50: [7.928830701700847e-06, 6.951078582763674e-06]},
        "bubble_sort": {
            50: [0.00012845424799804686, 0.00011387420361328127],
            100: [0.0004576137537760417, 0.00040870740234375],
        },
    }
    size, _ = results.greatest_common_size(input_data)
    expected = 50
    assert size == expected


def test_compare(capsys):
    """Test if comparison functions correctly"""
    size = 100
    experiment_data = {
        "insertion_sort": [1.436614706624349e-05, 1.3248109497070312e-05],
        "bubble_sort": [0.0004576137537760417, 0.00040870740234375],
    }
    results.compare(size, experiment_data)
    standard_out = capsys.readouterr()
    assert standard_out is not None
