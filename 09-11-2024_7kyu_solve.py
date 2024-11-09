"""In this Kata, you will be given an array of unique elements, and your task is to rearrange the values so that the first max value is followed by the first minimum, followed by second max value then second min value, etc.

For example:

solve([15,11,10,7,12]) = [15,7,12,10,11]
The first max is 15 and the first min is 7. The second max is 12 and the second min is 10 and so on.

More examples in the test cases.

Good luck!

"""
def solve(arr):
    sorted_arr = sorted(arr)
    return [sorted_arr.pop() if i%2==0 else sorted_arr.pop(0) for i in range(len(sorted_arr))]