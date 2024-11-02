#!/usr/bin/python
from helpers import assert_equals

"""
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.
Example:
h = 0
m = 1
s = 1

result = 61000
"""


def past(h, m, s):
    # Good Luck!
    return (h * 3600 + m * 60 + s) * 1000


if __name__ == "__main__":
    assert_equals(past(0, 1, 1), 61000)
    assert_equals(past(1, 1, 1), 3661000)
    assert_equals(past(0, 0, 0), 0)
    assert_equals(past(1, 0, 1), 3601000)
