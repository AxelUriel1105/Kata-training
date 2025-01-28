"""Complete the code which should return true if the given object is a single ASCII letter (lower or upper case), false otherwise.

"""
import string
def is_letter(s):
    return s in string.ascii_letters and len(s) == 1