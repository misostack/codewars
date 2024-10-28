#!/usr/bin/python
from helpers import assert_equals
"""

Write function bmi that calculates body mass index (bmi = weight / height2).
if bmi <= 18.5 return "Underweight"
if bmi <= 25.0 return "Normal"
if bmi <= 30.0 return "Overweight"
if bmi > 30 return "Obese"

"""

def bmi(weight, height):
    #your code here
    bmi = weight/ (height**2)
    if bmi <= 18.5:
        return "Underweight"
    if bmi <= 25.0:
        return "Normal"
    if bmi <= 30.0:
        return "Overweight"
    if bmi > 30:
        return "Obese"
    return None

if __name__ == "__main__":
    assert_equals(bmi(50, 1.80), "Underweight", "For weight = 50 and height = 1.80")
    assert_equals(bmi(80, 1.80), "Normal", "For weight = 80 and height = 1.80")
    assert_equals(bmi(90, 1.80), "Overweight", "For weight = 90 and height = 1.80")
    assert_equals(bmi(100, 1.80), "Obese", "For weight = 100 and height = 1.80")