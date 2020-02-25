"""Handle the arguments provided to Tada"""

import argparse

from . import constants


def parse(args):
    """Use argparse to parse provided command-line arguments"""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        epilog='''Sample usage: python3 tada_a_bigoh.py --directory
            /Users/myname/projectdirectory
            --module modulename.file --function function_name --types int"''',
    )

    # add all of the arguments to the command-line interface
    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="Package directory with functions to analyze",
    )
    parser.add_argument(
        "--module",
        required=True,
        type=str,
        help="Module name with functions to analyze",
    )
    parser.add_argument(
        "--function",
        required=True,
        type=str,
        help="Name of the module's function to analyze",
    )
    parser.add_argument(
        "--types",
        required=True,
        type=str,
        nargs="+",
        help="""Parameter types for function to analyze, hypothesis""",
    )
    parser.add_argument(
        "--schema", required=False, type=str, help="The path to the jsonschema",
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
        help="Maximum rounds of experiment",
    )
    parser.add_argument(
        "--runningtime",
        required=False,
        type=int,
        default=constants.RUNNINGTIME,
        help="Maximum running time",
    )
    parser.add_argument(
        "--expect",
        required=False,
        type=str,
        help="Expected Growth Ratio: O(1) O(logn) O(n) O(nlogn) O(n^2) O(n^3) O(c^n)",
    )
    parser.add_argument(
        "--backfill",
        required=False,
        type=int,
        default=constants.BACKFILL,
        help="Backfill if value equals 1",
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
        help="Largest size of the doubling experiment",
    )
    parser.add_argument(
        "--sortinput",
        required=False,
        type=int,
        default=constants.SORT,
        help="Sort input if value equals 1",
    )
    # parse the arguments and return the finished result
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args):
    """Verify the command-line arguments"""
    verified_arguments = False
    # CHECK: directory was specified and it is not ""
    if args.directory is not constants.NONE:
        verified_arguments = True
    # CHECK: module was specified and it is not ""
    if args.module is not constants.NONE:
        verified_arguments = True
    # CHECK: function was specified and it is not ""
    if args.function is not constants.NONE:
        verified_arguments = True
    # CHECK: type was specified and it is not ""
    if args.function is not constants.NONE:
        verified_arguments = True
    return verified_arguments
