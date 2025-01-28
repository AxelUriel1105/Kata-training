"""Definition
A number is a Special Number if it’s digits only consist 0, 1, 2, 3, 4 or 5

Given a number determine if it special number or not .

Warm-up (Highly recommended)
Playing With Numbers Series
"""
def     (number):
    return ('NOT!!','Special!!')[all(n in '012345' for n in str(number))]