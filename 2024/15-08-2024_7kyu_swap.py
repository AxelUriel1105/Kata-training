"""When provided with a String, capitalize all vowels

For example:

Input : "Hello World!"

Output : "HEllO WOrld!"

Note: Y is not a vowel in this kata.

"""
def swap(st):
    return "".join(l.upper() if l in ('aeiou') else l for l in st)