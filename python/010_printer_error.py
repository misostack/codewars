#!/usr/bin/python
from helpers import assert_equals

"""
In a factory a printer prints labels for boxes. 
For one kind of boxes the printer has to use colors which, for the sake of simplicity, are named with letters from a to m.

The colors used by the printer are recorded in a control string. 
For example a "good" control string would be aaabbbbhaijjjm meaning that the printer used three times color a, four times color b, one time color h then one time color a...

Sometimes there are problems: lack of colors, technical malfunction and a "bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not from a to m.

You have to write a function printer_error which given a string will return the error rate of the printer as a string representing a rational whose numerator is the number of errors and the denominator the length of the control string. Don't reduce this fraction to a simpler expression.

The string has a length greater or equal to one and contains only letters from ato z.

s="aaabbbbhaijjjm"
printer_error(s) => "0/14"

s="aaaxbbbbyyhwawiwjjjwwm"
printer_error(s) => "8/22"

"""

print('w' < 'a')
print('w' > 'm')

print([c for c in "abcz1" if c < 'a' or c > 'c' ])

def printer_error(s):
    
    invalids = [c for c in s if c < 'a' or c > 'm']
    return f"{len(invalids)}/{len(s)}"
    


if __name__ == "__main__":
    s = "aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    assert_equals(printer_error(s), "3/56")
    s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    assert_equals(printer_error(s), "6/60")
    s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
    assert_equals(printer_error(s), "11/65")
