"""Complete the function which converts a binary number (given as a string) to a decimal number.

"""
import math
def bin_to_decimal(inp):
    return  int(sum(math.pow(2,i) for i in range(0,len(inp)) if inp[::-1][i] != "0"))