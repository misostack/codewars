#!/usr/bin/python
from helpers import assert_equals

"""
Take 2 strings s1 and s2 including only letters from a to z. 
Return a new sorted string (alphabetical ascending), the longest possible, 
containing distinct letters - each taken only once - coming from s1 or s2.

a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"
"""

# from functools import reduce

def longest(a1, a2):
    # your code
    alphabet = [chr(c) for c in range(ord('a'), ord('z')) if a1.count(chr(c)) or a2.count(chr(c)) ]
    alphabet.append('z') if a1.count('z') or a2.count('z') else None
    s = ''
    for c in alphabet:
        s += c
    return s
    # return reduce(lambda x,y: x+y, alphabet)
    


if __name__ == "__main__":
    assert_equals(longest("aretheyhere", "yestheyarehere"), "aehrsty")
    assert_equals(longest("loopingisfunbutdangerous", "lessdangerousthancoding"), "abcdefghilnoprstu")
    assert_equals(longest("inmanylanguages", "theresapairoffunctions"), "acefghilmnoprstuy")
