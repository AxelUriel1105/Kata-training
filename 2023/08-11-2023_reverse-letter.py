"""For str = "krishan", the output should be "nahsirk".

For str = "ultr53o?n", the output should be "nortlu".

Input/Output
[input] string str
A string consists of lowercase latin letters, digits and symbols.

[output] a string"""
import string
def reverse_letter(letter):
    return "".join(i for i in letter if i in string.ascii_lowercase)[::-1]
