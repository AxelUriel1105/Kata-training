"""In this kata the aim is to compare each pair of integers from two arrays, and return a new array of large numbers.

Note: Both arrays have the same dimensions.

Example:
arr1 = [13, 64, 15, 17, 88]
arr2 = [23, 14, 53, 17, 80]
get_larger_numbers(arr1, arr2) == [23, 64, 53, 17, 88]"""
def get_larger_numbers(a, b):
    return [(i1,i2)[i1<i2] for i1,i2 in zip(a,b)]