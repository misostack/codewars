#!/usr/bin/python
from helpers import assert_equals

"""
Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case insensitive. The string can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false

"""


def xo(s):
    # s = s.lower()
    # return s.count('x') == s.count('o')    
    x_count, o_count = 0, 0
    for c in s:
        x_count += c.lower() == 'x'
        o_count += c.lower() == 'o'
    return x_count == o_count

if __name__ == "__main__":
    test_cases = [
        ("ooxx",    True),
        ("xooxx",   False),
        ("ooxXm",   True),  # Comparison is case-insensitive
        ("zpzpzpp", True),  # when no 'x' and 'o' is present should return true
        ("zzoo",    False),
        ("oxOx",    True),
        ("",        True),  # Empty string contains equal amount of x and o
    ]
    for s, expected in test_cases:
        assert_equals(xo(s), expected)
