#!/usr/bin/python
from helpers import assert_equals

"""
"Robin Singh" ==> ["Robin", "Singh"]

"I love arrays they are my favorite" ==> ["I", "love", "arrays", "they", "are", "my", "favorite"]
"""

def string_to_array(s):
    # your code here
    return s.split(" ")

if __name__ == "__main__":
    assert_equals(string_to_array("Robin Singh"), ["Robin", "Singh"])
    assert_equals(string_to_array("CodeWars"), ["CodeWars"])
    assert_equals(string_to_array("I love arrays they are my favorite"), ["I", "love", "arrays", "they", "are", "my", "favorite"])
    assert_equals(string_to_array("1 2 3"), ["1", "2", "3"])
    assert_equals(string_to_array(""), [""])