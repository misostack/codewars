#!/usr/bin/python
from helpers import assert_equals

"""
Implement a function that adds two numbers together and returns their sum in binary. The conversion can be done before, or after the addition.

The binary number returned should be a string.

Examples:(Input1, Input2 --> Output (explanation)))

1, 1 --> "10" (1 + 1 = 2 in decimal or 10 in binary)
5, 9 --> "1110" (5 + 9 = 14 in decimal or 1110 in binary)
"""

"""
To convert a decimal number to binary, you need to follow these steps:
Divide the decimal number by 2 and write down the integer result (ignore the remainder).
Repeat step 1 with the integer result until you get 0.
Write down the remainders (in reverse order) of each division as 0 or 1 to get the binary equivalent.
"""

def decimal_to_bin(n):
    binary_value = ''
    while n != 0:
        binary_value = f"{n%2}{binary_value}"
        n = n//2
    
    return binary_value

def add_binary(a, b):
    # your code here
    return bin(a+b).replace("0b", "")

if __name__ == "__main__":
    assert_equals(add_binary(1, 1), "10")
    assert_equals(add_binary(0, 1), "1")
    assert_equals(add_binary(1, 0), "1")
    assert_equals(add_binary(2, 2), "100")
    assert_equals(add_binary(51, 12), "111111")
