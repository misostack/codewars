
#!/usr/bin/python
from helpers import assert_equals

"""
Write a function that accepts an integer n and a string s as parameters, and returns a string of s repeated exactly n times.

6, "I"     -> "IIIIII"
5, "Hello" -> "HelloHelloHelloHelloHello"
"""


def repeat_str(repeat, string):
    return string * repeat


if __name__ == "__main__":
    assert_equals(repeat_str(4, 'a'), 'aaaa')
    assert_equals(repeat_str(3, 'hello '), 'hello hello hello ')
    assert_equals(repeat_str(2, 'abc'), 'abcabc')
