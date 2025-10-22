"""Create a function that receives a string consists of only digit characters ('0' to '9'), and returns the lowest product of 4 consecutive digits within that string.

This should only work if the number has 4 digits or more. If not, return "Number is too small" instead.

Example
"123456789" --> 24    // 1*2*3*4
"35" --> "Number is too small"
"""
import numpy as np
def lowest_product(num):
    products = [np.prod(list(map(int,num[i:i+4]))) for i in range(len(num)) if len(num[i:i+4]) == 4]
    return min(products) if len(num) >= 4 else 'Number is too small'