"""In this Kata, you will be given a string and your task will be to return a list of ints detailing the count of uppercase letters, lowercase, numbers and special characters, as follows.

Solve("*'&ABCDabcde12345") = [4,5,5,3]. 
--the order is: uppercase letters, lowercase, numbers and special characters.
More examples in the test cases.

Good luck!"""
import string
def solve(s):
    uppercase = sum(1 for i in s if i in string.ascii_uppercase)
    lowercase = sum(1 for i in s if i in string.ascii_lowercase)
    nums = sum(1 for n in s if n in '0123456789')
    return [uppercase,lowercase, nums, len(s)-uppercase-lowercase-nums]