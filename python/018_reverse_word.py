#!/usr/bin/python
from helpers import assert_equals

"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
  return " ".join([w[::-1] for w in text.split(" ")])
  words = text.split(" ")
  reversed_values = []
  for w in words:
      chars = [c for c in w]
      chars.reverse()
      reversed_values.append("".join(chars))
  return " ".join(reversed_values)
        


if __name__ == "__main__":
    assert_equals(reverse_words('The quick brown fox jumps over the lazy dog.'),
                  'ehT kciuq nworb xof spmuj revo eht yzal .god')
    assert_equals(reverse_words('apple'), 'elppa')
    assert_equals(reverse_words('a b c d'), 'a b c d')
    assert_equals(reverse_words('double  spaced  words'),
                  'elbuod  decaps  sdrow')
