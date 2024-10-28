#!/usr/bin/python
from helpers import assert_equals

"""
Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives become positives.
[1, 2, 3, 4, 5] --> [-1, -2, -3, -4, -5]
[1, -2, 3, -4, 5] --> [-1, 2, -3, 4, -5]
[] --> []
"""

def invert(lst):
    return [-1 * i for i in lst]

if __name__ == "__main__":
    assert_equals(invert([1,2,3,4,5]),[-1,-2,-3,-4,-5])
    assert_equals(invert([1,-2,3,-4,5]), [-1,2,-3,4,-5])
    assert_equals(invert([]), [])