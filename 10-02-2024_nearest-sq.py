"""Your task is to find the nearest square number, nearest_sq(n) or nearestSq(n),
 of a positive integer n.

For example, if n = 111, then nearest\_sq(n) (nearestSq(n)) equals 121, since 111 is
 closer to 121, the square of 11, than 100, the square of 10.

If the n is already the perfect square (e.g. n = 144, n = 81, etc.), you need to just return n.

Good luck :)

Check my other katas:"""

import math
def nearest_sq(n):
    sqrtInf = int(math.sqrt(n))**2
    sqrtSup = math.ceil(math.sqrt(n))**2
    return  sqrtInf if abs(sqrtInf - n) < abs(sqrtSup - n) else sqrtSup