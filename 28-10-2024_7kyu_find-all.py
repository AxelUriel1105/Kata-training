"""If n is not in the given array, return an empty array [].

Assume that n and all values in the given array will always be integers.

Example:

find_all([6, 9, 3, 4, 3, 82, 11], 3)
> [2, 4]
"""
def find_all(array, n):
    return [index for index,e in enumerate(array) if e == n]