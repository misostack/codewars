#!/usr/bin/python
from helpers import assert_equals
import math

"""
You might know some pretty large perfect squares. But what about the NEXT one?

Complete the findNextSquare method that finds the next integral 
perfect square after the one passed as a parameter. 
Recall that an integral perfect square is an integer n 
such that sqrt(n) is also an integer.

If the argument is itself not a perfect square then return either -1 
or an empty value like None or null, depending on your language. 
You may assume the argument is non-negative.

Examples ( Input --> Output )

121 --> 144
625 --> 676
114 --> -1  #  because 114 is not a perfect square
"""


def find_next_square(sq):
    # Return the next square if sq is a square, -1 otherwise
    v = math.sqrt(sq)
    is_not_integer = v % 1
    if is_not_integer:
          return -1
    return (v + 1)**2


if __name__ == "__main__":
        assert_equals(find_next_square(114), -1, "Wrong output for 121")
        assert_equals(find_next_square(121), 144, "Wrong output for 121")
        assert_equals(find_next_square(625), 676, "Wrong output for 625")
        assert_equals(find_next_square(319225), 320356, "Wrong output for 319225")
        assert_equals(find_next_square(15241383936), 15241630849, "Wrong output for 15241383936")
        assert_equals(find_next_square(155), -1, "Wrong output for 155")
        assert_equals(find_next_square(342786627), -1, "Wrong output for 342786627")        
