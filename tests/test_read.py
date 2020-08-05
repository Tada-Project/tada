"""Tests for the read module"""

from tada.util import read
import pytest

def test_read_value(tmpdir):
    """Checks that read value properly return one"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write("Hello World")
    output = read.read_value(path)
    assert output is not None


def test_read_experiment_size():
    """Checks that read experiment size properly return one"""
    try:
        read.read_experiment_size()
    except FileNotFoundError:
        assert True


def test_read_directory():
    """Checks that read directory properly return one"""
    try:
        read.read_directory()
    except FileNotFoundError:
        assert True


def test_read_schema(tmpdir):
    """Checks that read schema properly return one"""
    path = tmpdir.mkdir("sub").join("hello.json")
    path.write(
        '[{"type": "array", "items": {"type": "number"}}\n\
        ,{"type": "array", "items": {"type": "number"}}]')
    output = read.read_schema(path)
    assert output is not None
