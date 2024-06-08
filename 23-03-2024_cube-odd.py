"""Find the sum of the odd numbers within an array, after cubing the initial 
integers. The function should return undefined/None/nil/NULL if any of the values aren't numbers.

Note: Booleans should not be considered as numbers."""
def cube_odd(arr):
    for i in arr: 
        if str(i) == 'True' or i == 'False':
            return None
    try:
        return sum(i**3 for i in arr if i%2 != 0)
    except:
        return None