"""Tests for the read module"""

from tada.util import read


def test_read_value(tmpdir):
    """Checks that read value properly return one"""
    path = tmpdir.mkdir("sub").join("hello.txt")
    path.write("Hello World")
    output = read.read_value(path)
    assert output is not None
