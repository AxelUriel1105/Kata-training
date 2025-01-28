"""Move every letter in the provided string forward 10 letters through the alphabet.

If it goes past 'z', start again at 'a'.

Input will be a string with length > 0."""
import string
def move_ten(st):
    alphabet = dict(zip(string.ascii_lowercase,range(26)))
    alphabet2 = dict(zip(range(26), string.ascii_lowercase))
    return ''.join(alphabet2.get((alphabet.get(l)+10)%26) for l in st)