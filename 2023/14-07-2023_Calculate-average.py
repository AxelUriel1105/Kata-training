"""Write a function which calculates the average of the numbers in a given list.

Note: Empty arrays should return 0."""
def find_average(numbers):
    SUM = sum(numbers)
    count = 0 
    for i in numbers:
        count+= 1
    if numbers != []:
        return SUM/count 
    else: 
        return 0
    
find = find_average([1,2,3,4,5])
print (find)

