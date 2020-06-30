"""Tests for the read module"""

from tada.util import read


def test_read_experiment_size():
    """Checks that read experimnet size properly return one"""
    size = read.read_experiment_size()
    assert size is not None


def test_read_directory_size():
    """Checks that read directory properly return one"""
    directory = read.read_directory()
    assert directory is not None
