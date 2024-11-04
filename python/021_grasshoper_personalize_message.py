
#!/usr/bin/python
from helpers import assert_equals
import math

"""
Create a function that gives a personalized greeting. This function takes two parameters: name and owner.

Use conditionals to return the proper message:

name equals owner => 'Hello boss'
otherwise => 'Hello guest'
"""


def greet(name, owner):
    # Add code here
    greet_name = 'boss' if name == owner else 'guest'
    return f'Hello {greet_name}'


if __name__ == "__main__":
    assert_equals(greet('Daniel', 'Daniel'), 'Hello boss')
    assert_equals(greet('Greg', 'Daniel'), 'Hello guest')
