#!/usr/bin/python
from helpers import assert_equals

# Given a string, you have to return a string in which each character (case-sensitive) is repeated once.
# * "String"      -> "SSttrriinngg"
# * "Hello World" -> "HHeelllloo  WWoorrlldd"
# * "1234!_ "     -> "11223344!!__  "

print(ord('A'), ord('a'))
print('A' < 'a')

def double_char(s):
    new_s = ''
    for c in s:
        # is uppercase
        new_s += c + c
    return new_s


if __name__ == "__main__":
    assert_equals(double_char("String"), "SSttrriinngg")
    assert_equals(double_char("Hello World"), "HHeelllloo  WWoorrlldd")
    assert_equals(double_char("1234!_ "), "11223344!!__  ")
    pass