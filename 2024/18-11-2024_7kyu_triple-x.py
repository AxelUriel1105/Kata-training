"""Given a string, return true if the first instance of "x" in the string is immediately followed by the string "xx".

"abraxxxas" → true
"xoxotrololololololoxxx" → false
"softX kitty, warm kitty, xxxxx" → true
"softx kitty, warm kitty, xxxxx" → false
Note :

capital X's do not count as an occurrence of "x".
if there are no "x"'s then return false"""
def triple_x(s):
    try:
        first_x = s.index('x')
        return s[first_x:first_x+3] == 'xxx'
    except:
        return False