"""Create a function that takes a string as a parameter and does the following, in this order:

Replaces every letter with the letter following it in the alphabet (see note below)
Makes any vowels capital
Makes any consonants lower case
Note:

the alphabet should wrap around, so Z becomes A
in this kata, y isn't considered as a vowel.
So, for example the string "Cat30" would return "dbU30" (Cat30 --> Dbu30 --> dbU30)"""
import string 
def changer(s):
    alphabet = string.ascii_lowercase
    alphabet_dict = dict(zip(alphabet,alphabet[1::]+'a'))
    replace_letters = ''.join(alphabet_dict.get(c,c) for c in s.lower())
    return ''.join(c.upper() if c in 'aeiou' else c for c in replace_letters)