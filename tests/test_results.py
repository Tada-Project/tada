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
    expect = """ Size | Mean | Median | Ratio \n------|------|--------|-------"""
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
