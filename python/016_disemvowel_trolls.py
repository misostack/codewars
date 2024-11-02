#!/usr/bin/python
from helpers import assert_equals

"""
Trolls are attacking your comment section!

A common way to deal with this situation is to remove all of the vowels from the trolls' comments, neutralizing the threat.

Your task is to write a function that takes a string and return a new string with all vowels removed.

For example, the string "This website is for losers LOL!" would become "Ths wbst s fr lsrs LL!".

Note: for this kata y isn't considered a vowel.

"""
import re

def disemvowel(string_):
    # return re.sub("[aeiouAEIOU]", '', string_)
    for vowel in ['a','e','i','o','u']:
        string_ = string_.replace(vowel, '')
        string_ = string_.replace(vowel.upper(), '')
    return string_
    # return "".join(c for c in string_ if c.lower() not in "aeiou")


if __name__ == "__main__":
    assert_equals(disemvowel("This website is for losers LOL!"), "Ths wbst s fr lsrs LL!",
                  'Incorrect answer for input="This website is for losers LOL!"\n')
    assert_equals(disemvowel("No offense but,\nYour writing is among the worst I've ever read"), "N ffns bt,\nYr wrtng s mng th wrst 'v vr rd",
                  'Incorrect answer for input="No offense but,\nYour writing is among the worst I\'ve ever read"\n')
    assert_equals(disemvowel("What are you, a communist?"), "Wht r y,  cmmnst?",
                  'Incorrect answer for input="What are you, a communist?"\n')
