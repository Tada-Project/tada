"""Handle the arguments provided to Tada"""

import argparse


def parse(args):
    """Use argparse to parse provided command-line arguments"""
    # create the parser with the default help formatter
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
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
    # parse the arguments and return the finished result
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args):
    """Verify the command-line arguments"""
    verified_arguments = False
    # CHECK: directory was specified and it is not ""
    if args.directory is not "":
        verified_arguments = True
    # CHECK: module was specified and it is not ""
    if args.module is not "":
        verified_arguments = True
    # CHECK: function was specified and it is not ""
    if args.function is not "":
        verified_arguments = True
    return verified_arguments
