"""Given a string as input, move all of its vowels to the end of the string, in the same order as they were before.

Vowels are (in this kata): a, e, i, o, u

Note: all provided input strings are lowercase.

Examples
"day"    ==>  "dya"
"apple"  ==>  "pplae"
"""
def move_vowels(s): 
    return  ''.join(c for c in s if c not in 'aeiou') + ''.join(v for v in s if v in 'aeiou')
    