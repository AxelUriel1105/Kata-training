"""Complete the solution so that the function will break up camel casing, using a space between words.

Example
"camelCasing"  =>  "camel Casing"
"identifier"   =>  "identifier"
""             =>  """
import string 


def solution(s):
    Upper = string.ascii_uppercase
    StringList = []
    for char in s:
        if char in Upper:
            StringList.append(" " + char)
        else:
            StringList.append(char)
            

    return "".join(StringList)
