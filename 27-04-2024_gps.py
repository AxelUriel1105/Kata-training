"""With the above data your function gps(s, x) should return 74

Note
With floats it can happen that results depends on the operations order. To calculate hourly
 speed you can use:

 (3600 * delta_distance) / s."""
from math import floor
def gps(s, x):
    try:
        AVG_speed = [((j-i)*3600)/s for i,j in zip(x,x[1::])]
        return floor(max(AVG_speed))
    except:
        return 0