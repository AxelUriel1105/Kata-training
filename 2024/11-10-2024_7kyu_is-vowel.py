"""Implement the function which should return true if given object is a vowel 
(meaning a, e, i, o, u, uppercase or lowercase), and false otherwise."""
def is_vowel(s): 
    return s in 'aeiouAEIOU' and len(s) == 1