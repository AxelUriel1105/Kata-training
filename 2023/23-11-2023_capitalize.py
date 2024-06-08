"""Given a string, capitalize the letters that occupy even indexes and odd indexes
 separately, and return as shown below. Index 0 will be considered even.

For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. See test cases for more examples.

The input will be a lowercase string with no spaces.

Good luck!

If you like this Kata, please try:

Indexed capitalization

Even-odd disparity"""
def capitalize(s):
    even = "".join([j.upper() if i%2 == 0 else j for i,j in enumerate(s)])
    odd = "".join([j.upper() if i%2 != 0 else j for i,j in enumerate(s)])
    return [even,odd]