"""An array of integers is defined to be odd-heavy if it contains at least one odd element and every odd number in it is greater than any even number in it.

Write a function that accepts an integer array and returns whether the array is odd-heavy.

Examples
Array [11,4,9,2,8] is odd-heavy,
because its odd elements [11,9] are greater than all the even elements [4,2,8]

Array [11,4,9,2,3,10] is not odd-heavy,
because one of its even elements (10 from [4,2,10]) is greater than two of
its odd elements (9 and 3 from [11,9,3])

Array [] is not odd-heavy,
because it does not contain any odd numbers

Array [3] is odd-heavy,
because it does not contain any even numbers."""
def is_odd_heavy(arr):
    try:
        return min(filter(lambda x: x%2!=0, arr)) > max(filter(lambda x: x%2==0,arr))
    except:
        return len(list(filter(lambda x: x%2!=0, arr))) > 0
