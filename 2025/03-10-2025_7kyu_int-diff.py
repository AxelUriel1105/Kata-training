"""Write a function that accepts two arguments: an array/list of integers and another integer (n).

Determine the number of times where two integers in the array have a difference of n.

For example:

[1, 1, 5, 6, 9, 16, 27], n=4  -->  3  # (1,5), (1,5), (5,9)
[1, 1, 3, 3], n=2             -->  4  # (1,3), (1,3), (1,3), (1,3)
"""
def int_diff(lst, n):
    if n < 0: return 0
    return sum(lst[index+1::].count(num-n) + lst[index+1::].count(n+num) if n!=0 else lst[index+1::].count(n+num) for index,num in enumerate(lst))