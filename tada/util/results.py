"""Results Table for Tada and perf."""

from __future__ import division
from typing import Union, Dict, List
from prettytable import PrettyTable
from . import analysis
from . import display as dis


def add_resultstable(
        resultstable: PrettyTable,
        current_size: int,
        mean: float,
        median: float,
        ratio: Union[int, float],
) -> None:
    """Add elements into the resultstable."""
    resultstable.add_row([current_size, mean, median, ratio])


def display_resultstable(resultstable: PrettyTable, to_md: bool = False) -> None:
    """Print out the resultstable."""
    if to_md:
        print(to_markdown_table(resultstable))
    else:
        print(resultstable)


def to_markdown_table(pt):
    """Convert prettytable to markdown format"""
    _junc = pt.junction_char
    if _junc != "|":
        pt.junction_char = "|"
    markdown = [row[1:-1] for row in pt.get_string().split("\n")[1:-1]]
    pt.junction_char = _junc
    return "\n".join(markdown)


def greatest_common_size(results):
    """Find the greatest common size of two experiments"""
    record_keys = list(results.keys())
    records = list(results.values())
    size = min(list(records[0].keys())[-1], list(records[1].keys())[-1])
    return size, {record_keys[0]: records[0][size], record_keys[1]: records[1][size]}


def compare(size, results: List[Dict[str, List[float]]]) -> None:
    """Compares the mean and median results of the two experiments"""
    # Get experiment names and results
    experiment_lst = list(results.keys())
    result_lst = list(results.values())
    mean_perc = (result_lst[0][0] / result_lst[1][0]) - 1
    median_perc = (result_lst[0][1] / result_lst[1][1]) - 1
    mean_result = dis.magenta("faster") if mean_perc < 0 else dis.red("slower")
    median_result = dis.magenta("faster") if median_perc < 0 else dis.red("slower")
    # Format to percentage
    mean_perc = "{:.2%}".format(abs(mean_perc))
    median_perc = "{:.2%}".format(abs(median_perc))
    # Display
    print("\nAt the greatest common size " + dis.cyan(size) + ":")
    print(
        dis.green("Mean: ")
        + f"{experiment_lst[0]} is {mean_perc} "
        + mean_result
        + f" than {experiment_lst[1]}"
    )
    print(
        dis.green("Median: ")
        + f"{experiment_lst[0]} is {median_perc} "
        + median_result
        + f" than {experiment_lst[1]}\n"
    )


def contrast(results):
    """Contrast two result tables"""
    # size, _ = greatest_common_size(results)
    contrast_table = PrettyTable()
    contrast_table.field_names = ["Size", "Mean", "Median", "Ratio"]
    record_keys = list(results.keys())
    records = list(results.values())
    rounds = list(records[0].keys())
    first_table = list(records[0].values())
    second_table = list(records[1].values())
    min_rounds = min(len(first_table), len(second_table))
    for i in range(min_rounds):
        mean = abs(second_table[i][0] - first_table[i][0])
        median = abs(second_table[i][1] - first_table[i][1])
        mean_lastround = mean
        if i == 0:
            ratio = 0
        else:
            ratio = mean / mean_lastround
        add_resultstable(contrast_table, rounds[i], mean, median, ratio)
        mean_lastround = mean
        big_oh = analysis.analyze_big_oh(ratio)
    contrast_table.title = (
        "Contrast for "
        + dis.blue(record_keys[0])
        + " and "
        + dis.red(record_keys[1])
        + ": "
        + big_oh
    )
    print(contrast_table)
