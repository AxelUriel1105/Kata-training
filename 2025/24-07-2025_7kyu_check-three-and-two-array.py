"""Given an array with exactly 5 strings "a", "b" or "c" (chars in Java, characters in Fortran, Chars in Haskell), check if the array contains three and two of the same values.

Examples
["a", "a", "a", "b", "b"] ==> true  // 3x "a" and 2x "b"
["a", "b", "c", "b", "c"] ==> false // 1x "a", 2x "b" and 2x "c"
["a", "a", "a", "a", "a"] ==> false // 5x "a"
"""
def check_three_and_two(array):
    sorted_arr = sorted(array, key=lambda x: array.count(x))
    return array.count(sorted_arr[0]) == 2 and array.count(sorted_arr[-1]) == 3