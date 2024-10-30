#!/usr/bin/python
from helpers import assert_equals

"""
Your classmates asked you to copy some paperwork for them. 
You know that there are 'n' classmates and the paperwork has 'm' pages.

Your task is to calculate how many blank pages do you need. If n < 0 or m < 0 return 0.

n= 5, m=5: 25
n=-5, m=5:  0

"""


def paperwork(n, m):
    # return 0 if n < 0 or m < 0 else n * m
    # Happy Coding! ^_^
    if n < 0 or m < 0:
        return 0
    return n * m


if __name__ == "__main__":
    assert_equals(paperwork(5, 5), 25, "Failed at Paperwork(5,5)")
    assert_equals(paperwork(1, 2), 2, "Failed at Paperwork(1,2)")
    assert_equals(paperwork(-5, 5), 0, "Failed at Paperwork(-5,5)")
    assert_equals(paperwork(5, -5), 0, "Failed at Paperwork(5,-5)")
    assert_equals(paperwork(-5, -5), 0, "Failed at Paperwork(-5,-5)")
    assert_equals(paperwork(5, 0), 0, "Failed at Paperwork(5,0)")
