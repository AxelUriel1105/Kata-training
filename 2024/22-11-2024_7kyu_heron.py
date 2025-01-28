"""Write function heron which calculates the area of a triangle with sides a, b, and c (x, y, z in COBOL).

Heron's formula:

s
∗
(
s
−
a
)
∗
(
s
−
b
)
∗
(
s
−
c
)
s∗(s−a)∗(s−b)∗(s−c)
​
 
where

s
=
a
+
b
+
c
2
s= 
2
a+b+c
​
 
Output should have 2 digits precision."""
import math
def heron(a, b, c):
    s = (a+b+c)/2
    return round(math.sqrt(s*(s-a)*(s-b)*(s-c)),2)