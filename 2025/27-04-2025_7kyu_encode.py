"""This is a follow up to my kata the old switcheroo.

Write a function that takes in a string and replaces all the letters with their respective positions in the English alphabet; e.g. 'a' is 1, 'z' is 26. The function should be case-insensitive.

'abc'      --> '123'
'ABC'      --> '123'
'codewars' --> '315452311819'
'abc-#@5'  --> '123-#@5'"""
import string
def encode(st):
    alphabet_dict = dict(zip(string.ascii_lowercase,range(1,27)))
    return ''.join(str(alphabet_dict.get(c.lower())) if c.lower() in alphabet_dict else c  for c in st)