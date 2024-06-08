"""Check to see if a string has the same amount of 'x's and 'o's. 
The method must return a boolean and be case insensitive. The string
 can contain any char.

Examples input/output:

XO("ooxx") => true
XO("xooxx") => false
XO("ooxXm") => true
XO("zpzpzpp") => true // when no 'x' and 'o' is present should return true
XO("zzoo") => false"""
from collections import Counter
def xo(s):
    s = s.lower()
    Dictionary = Counter(s)
    if "x" not in s and "o" not in s:
        return True
    elif Dictionary["x"] == Dictionary["o"]:
        return True
    else:
        return False