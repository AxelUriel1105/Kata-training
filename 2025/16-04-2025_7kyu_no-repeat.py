"""This Kata is intended as a small challenge for my students

All Star Code Challenge #16

Create a function called noRepeat() that takes a string argument and returns a single letter string of the first not repeated character in the entire string.

noRepeat("aabbccdde") // => "e"
noRepeat("wxyz") // => "w"
noRepeat("testing") // => "e"
Note: ONLY letters from the english alphabet will be used as input There will ALWAYS be at least one non-repeating letter in the input string

"""
from collections import Counter
def no_repeat(string):
    return sorted(Counter(string).items(), key=lambda x: (x[1],string.index(x[0])))[0][0]