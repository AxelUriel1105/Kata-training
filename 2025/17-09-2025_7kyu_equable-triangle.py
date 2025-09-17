"""A triangle is called an equable triangle if its area equals its perimeter.
 Return true, if it is an equable triangle, else return false. You will be provided
   with the length of sides of the triangle. Happy Coding!"""
def equable_triangle(a,b,c):
    s = (a+b+c)/2
    return (a+b+c) == (s*(s-a)*(s-b)*(s-c))**(1/2)