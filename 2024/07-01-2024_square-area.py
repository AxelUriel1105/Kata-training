"""Complete the function that calculates the area of the red square,
 when the length of the circular arc A is 
given as the input. Return the result rounded to two decimals."""
from math import pi
def square_area(A):
    return round((2*A/pi)**2,2)