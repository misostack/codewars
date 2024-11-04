
#!/usr/bin/python
from helpers import assert_equals
import math

"""
Sum all the numbers of a given array ( cq. list ), except the highest and the lowest element ( by value, not by index! ).

The highest or lowest element respectively is a single element at each edge, even if there are more than one with the same value.

Mind the input validation.

{ 6, 2, 1, 8, 10 } => 16
{ 1, 1, 11, 2, 3 } => 6
"""


def sum_array(arr):
    if not arr:
        return 0
    # your code here
    arr = sorted(arr)
    slice = arr[1:-1]
    return sum(slice) if len(slice) > 0 else 0


if __name__ == "__main__":
    assert_equals(sum_array(None), 0)
    assert_equals(sum_array([]), 0)
    assert_equals(sum_array([3]), 0)
    assert_equals(sum_array([-3]), 0)
    assert_equals(sum_array([3, 5]), 0)
    assert_equals(sum_array([-3, -5]), 0)
    assert_equals(sum_array([6, 2, 1, 8, 10]), 16)
    assert_equals(sum_array([6, 0, 1, 10, 10]), 17)
    assert_equals(sum_array([-6, -20, -1, -10, -12]), -28)
    assert_equals(sum_array([-6, 20, -1, 10, -12]), 3)
