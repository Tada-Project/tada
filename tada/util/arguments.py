"""Handle the arguments provided to Tada"""

import sys
import argparse
import copy

from typing import List
from argparse import Namespace
from . import constants


def parse(args: List[str]) -> Namespace:
    """Use argparse to parse provided command-line arguments"""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog="""Sample usage: pipenv run python tada_a_bigoh.py --directory
            /Users/myname/projectdirectory
            --module modulename.file --function function_name --types hypothesis""",
    )

    # add all of the arguments to the command-line interface
    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        nargs="+",
        help="Path to the package directory with functions to analyze",
    )
    parser.add_argument(
        "--module",
        required=True,
        type=str,
        nargs="+",
        help="Module name with functions to analyze",
    )
    parser.add_argument(
        "--function",
        required=True,
        type=str,
        nargs="+",
        help="Name of the function to analyze",
    )
    parser.add_argument(
        "--types",
        required=True,
        type=str,
        nargs="+",
        help="""Data generation type: hypothesis or parameter types of the function""",
    )
    parser.add_argument(
        "--data_directory",
        required=False,
        type=str,
        help="Path to the package directory with function to generate data",
    )
    parser.add_argument(
        "--data_module",
        required=False,
        type=str,
        help="Module name with functions to generate data",
    )
    parser.add_argument(
        "--data_function",
        required=False,
        type=str,
        help="Name of the data generation function",
    )
    parser.add_argument(
        "--schema",
        required=False,
        type=str,
        help="The path to the JSON schema that describes the data format",
    )
    parser.add_argument(
        "--startsize",
        required=False,
        type=int,
        default=constants.SIZE_START,
        help="Starting size of the doubling experiment",
    )
    parser.add_argument(
        "--steps",
        required=False,
        type=int,
        default=constants.STEPS,
        help="Maximum rounds of the doubling experiment",
    )
    parser.add_argument(
        "--runningtime",
        required=False,
        type=int,
        default=constants.RUNNINGTIME,
        help="Maximum running time of the doubling experiment",
    )
    parser.add_argument(
        "--expect",
        required=False,
        type=str,
        help="""Expected Growth Ratio: O(1) | O(logn) | O(n) | O(nlogn) | O(n^2)
        | O(n^3) | O(c^n). By using this argument, the experiment result will be
        stored in a csv file""",
    )
    parser.add_argument(
        "--backfill",
        required=False,
        action="store_true",
        default=constants.BACKFILL,
        help="""Enable backfill to shrink experiments size according to the
        Predicted True Value""",
    )
    parser.add_argument(
        "--indicator",
        required=False,
        type=float,
        default=constants.INDICATOR,
        help="Indicator value",
    )
    parser.add_argument(
        "--maxsize",
        required=False,
        type=int,
        default=constants.MAX_SIZE,
        help="Maximum size of the doubling experiment",
    )
    parser.add_argument(
        "--sorted",
        required=False,
        action="store_true",
        default=constants.SORT,
        help="Enable input data to be sorted",
    )
    parser.add_argument(
        "--log",
        required=False,
        action="store_true",
        default=False,
        help="Show log/debug/diagnostic output",
    )
    parser.add_argument(
        "--md",
        required=False,
        action="store_true",
        default=False,
        help="Show results table in markdown format",
    )
    parser.add_argument(
        "--contrast",
        required=False,
        action="store_true",
        default=False,
        help="Show contrast result table. Only works with multiple experiments",
    )
    parser.add_argument(
        "--viz",
        required=False,
        action="store_true",
        default=False,
        help="Visualize a simple graph for the result",
    )
    parser.add_argument(
        "--level",
        required=False,
        type=int,
        default=constants.LEVEL,
        help="The level of nested data structure to apply doubling experiment",
    )
    parser.add_argument(
        "--position",
        required=False,
        nargs="+",
        type=int,
        default=constants.POSITION,
        help="""The position of input data to double in the multivariable
        doubling experiment. Must be the last argument""",
    )
    # parse the arguments and return the finished result
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args: Namespace) -> bool:
    """Verify the command-line arguments"""
    verified_arguments = False
    # CHECK: directory was specified and it is not ""
    if args.directory == constants.NONE_LIST:
        return verified_arguments
    # CHECK: module was specified and it is not ""
    if args.module == constants.NONE_LIST:
        return verified_arguments
    # CHECK: function was specified and it is not ""
    if args.function == constants.NONE_LIST:
        return verified_arguments
    # CHECK: type was specified and it is not ""
    if args.types == constants.NONE_LIST:
        return verified_arguments
    verified_arguments = True
    return verified_arguments


def parse_args(cmd: List[str]) -> List[Namespace]:
    """parse arguments with multiple experiments into seperate ones"""
    # parse terminal input
    arguments = parse(cmd)
    args_dict = vars(arguments)
    args_lst = [arguments.directory, arguments.module, arguments.function]

    arg_1 = copy.deepcopy(args_dict)
    arg_2 = copy.deepcopy(args_dict)
    arg_1["directory"] = arguments.directory[0]
    arg_1["module"] = arguments.module[0]
    arg_1["function"] = arguments.function[0]
    # return the argument object if only one function in one module
    # of one directory provided
    if any(len(arg) > 2 for arg in args_lst):
        print("\nComparison feature can only take two functions now\n")
        sys.exit()
    if all(len(arg) == 1 for arg in args_lst):
        return [argparse.Namespace(**arg_1)]

    # assume the single argument is true for both experiments
    if len(arguments.directory) > 1:
        arg_2["directory"] = arguments.directory[1]
    else:
        arg_2["directory"] = arguments.directory[0]
    if len(arguments.module) > 1:
        arg_2["module"] = arguments.module[1]
    else:
        arg_2["module"] = arguments.module[0]
    if len(arguments.function) > 1:
        arg_2["function"] = arguments.function[1]
    else:
        arg_2["function"] = arguments.function[0]

    arg_lst = [argparse.Namespace(**arg_1), argparse.Namespace(**arg_2)]
    return arg_lst
