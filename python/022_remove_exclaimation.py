
#!/usr/bin/python
from helpers import assert_equals

"""
Write function RemoveExclamationMarks which removes all exclamation marks from a given string.
"""

import re

def remove_exclamation_marks(s):
    # your code here
    return re.sub("[!]", '', s)


if __name__ == "__main__":
    assert_equals(remove_exclamation_marks("Hello World!"), "Hello World")
    assert_equals(remove_exclamation_marks("Hello World!!!"), "Hello World")
    assert_equals(remove_exclamation_marks("Hi! Hello!"), "Hi Hello")
    assert_equals(remove_exclamation_marks(""), "")
    assert_equals(remove_exclamation_marks("Oh, no!!!"), "Oh, no")
