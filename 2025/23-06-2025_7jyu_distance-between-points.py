"""This series of katas will introduce you to basics of doing geometry with computers.

Point objects have attributes x and y.

Write a function calculating distance between Point a and Point b.

Input coordinates fit in range 
−
50
⩽
x
,
y
⩽
50
−50⩽x,y⩽50. Tests compare expected result and actual answer with tolerance of 1e-6.

"""
def distance_between_points(a, b):
    return ((a.x-b.x)**2 + (a.y-b.y)**2)**(1/2)