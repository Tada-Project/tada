"""Package management for Tada"""

import sys


def add_sys_path(requested_path: str) -> None:
    """Add the requested_path to the sys.path"""
    sys.path.insert(0, requested_path)
