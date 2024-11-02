#!/usr/bin/python
from helpers import assert_equals

"""
Complete the square sum function so that it squares each number passed into it and then sums the results together.
For example, for [1, 2, 2] it should return 9
"""

from functools import reduce


def square_sum(numbers):
    # result = 0
    # for num in numbers:
    #     result += num**2
    # return result
    return sum(x**2 for x in numbers)
    # return reduce(lambda accu, current : accu + current**2, numbers, 0)


if __name__ == "__main__":
    assert_equals(square_sum([1, 2]), 5)
    assert_equals(square_sum([0, 3, 4, 5]), 50)
    assert_equals(square_sum([]), 0)
    assert_equals(square_sum([-1, -2]), 5)
    assert_equals(square_sum([-1, 0, 1]), 2)
