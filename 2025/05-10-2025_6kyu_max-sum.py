"""Description:
For example:

 Given arr = [1,-2,3,4,-5,-4,3,2,1], 
       range = [[1,3],[0,4],[6,8]]
 should return 6
 
 calculation process:
 range[1,3] = arr[1]+arr[2]+arr[3] = 5
 range[0,4] = arr[0]+arr[1]+arr[2]+arr[3]+arr[4] = 1
 range[6,8] = arr[6]+arr[7]+arr[8] = 6
 So the maximum sum value is 6
Note:
arr/$a always has at least 5 elements;
range/$range/ranges always has at least 1 element;
All inputs are valid;
This is a simple version, if you want some challenge, please try the challenge version.
Some Examples
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3],[0,4],[6,8]]) === 6
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,3]]) === 5
 maxSum([1,-2,3,4,-5,-4,3,2,1],[[1,4],[2,5]]) === 0"""
def max_sum(arr,ranges): 
    return max(sum_range(range_, arr) for range_ in ranges)
def sum_range(range_,arr):
    return sum(arr[index] for index in range(range_[0],range_[1]+1))