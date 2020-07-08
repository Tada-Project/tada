"""Tests for display module"""

from tada.util import display


def test_welcome_message():
    msg = display.welcome_message()
    assert msg is not None


def test_start_message():
    msg = display.start_message(10, "insertion_sort")
    msg = msg.split()
    assert "\x1b[36m\x1b[1m10\x1b[0m" in msg
    assert "\x1b[34m\x1b[1minsertion_sort\x1b[0m" in msg


def test_end_message():
    msg = display.end_message(10, "insertion_sort")
    msg = msg.split()
    assert "\x1b[36m\x1b[1m10\x1b[0m" in msg
    assert "\x1b[34m\x1b[1minsertion_sort\x1b[0m" in msg


def test_output_messgae():
    none_msg = display.output_message(None)
    assert none_msg is False
    print_msg = display.output_message("10", True)
    assert print_msg is True
