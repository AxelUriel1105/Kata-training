"""You are given an odd-length array of integers, in which all of them are the same,
 except for one single number.

Complete the method which accepts such an array, and returns that single different number.

The input array will always be valid! (odd-length >= 3)

Examples
[1, 1, 2] ==> 2
[17, 17, 3, 17, 17, 17, 17] ==> 3"""
def stray(arr):
    arr.sort()
    return arr[-1] if arr[-1] != arr[-2] else arr[0]