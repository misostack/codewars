#!/usr/bin/python
from helpers import assert_equals

"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr):
    # print(list(x for x in arr if x > 0))
    # return sum(x for x in arr if x > 0)
    # Your code here
    return sum(x if x >0 else 0 for x in arr)


if __name__ == "__main__":
    assert_equals(positive_sum([1, 2, 3, 4, 5]), 15)
    assert_equals(positive_sum([1, -2, 3, 4, 5]), 13)
    assert_equals(positive_sum([-1, 2, 3, 4, -5]), 9)
