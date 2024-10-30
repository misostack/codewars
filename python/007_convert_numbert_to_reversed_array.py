#!/usr/bin/python
from helpers import assert_equals

"""
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

Example(Input => Output):
35231 => [1,3,2,5,3]
0 => [0]

"""


def digitize(n):
    s = []
    for c in str(n):
        s.insert(0, int(c))
    return s

if __name__ == "__main__":
    assert_equals(digitize(35231),[1,3,2,5,3])
    assert_equals(digitize(0),[0])
    assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
    assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
    assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
    assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])
