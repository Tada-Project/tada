"""Handle the arguments provided to Tada"""

import argparse


def parse(args):
    """Use argparse to parse provided command-line arguments"""
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--directory",
        required=True,
        type=str,
        help="Package directory with functions to analyze",
    )
    arguments_finished = parser.parse_args(args)
    return arguments_finished


def verify(args):
    """Verify the command-line arguments"""
    verified_arguments = False
    if args.directory is not None:
        verified_arguments = True
    return verified_arguments
