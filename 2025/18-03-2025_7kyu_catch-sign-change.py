"""Count how often sign changes in array.

result
number from 0 to ... . Empty array returns 0

example
const arr = [1, -3, -4, 0, 5];

/*
| elem | count |
|------|-------|
|  1   |  0    |
| -3   |  1    |
| -4   |  1    |
|  0   |  2    |
|  5   |  2    |
*/

catchSignChange(arr) == 2;"""
def catch_sign_change(lst):
    return sum((n1 > 0 and n2 < 0) or (n1 < 0 and n2 > 0) or (n1 < 0 and n2 == 0) or (n1 == 0 and n2 < 0) for n1,n2 in zip(lst,lst[1::]))