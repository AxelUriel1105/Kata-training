"""An element in an array is dominant if it is greater than all elements to its right. You will be given an array and your task will be to return a list of all dominant elements. For example:

solve([1,21,4,7,5]) = [21,7,5] because 21, 7 and 5 are greater than elments to their right. 
solve([5,4,3,2,1]) = [5,4,3,2,1]

Notice that the last element is always included. All numbers wi"""
def solve(arr):
    domaint_list = [n for index,n in enumerate(arr) if max(arr[index:]) == n]
    return sorted(set(domaint_list),key = domaint_list.index)