"""The number 89 is the first integer with more than one digit that fulfills the
 property partially introduced in the title of this kata. What's the use of saying "Eureka"? 
 Because this sum gives the same number:
 89 = 8**1 + 9**2
 We need a function to collect these numbers, that may receive two integers a,b that defines the range 
[a,b] (inclusive) and outputs a list of the sorted numbers in the range that fulfills the property 
described above."""
def sum_dig_pow(a, b): # range(a, b + 1) will be studied by the function
    PowerList = []
    for i in range(a,b+1):
        clist = sum([int(k)**(j+1) for j,k in enumerate(str(i))])
        if clist == i:
            PowerList.append(i)
            
    return PowerList