
"""

Write a function that removes every lone 9 that is inbetween 7s.

"79712312" --> "7712312"
"79797"    --> "777"
"""
def seven_ate9(str_):
    s = ''
    for index, n in enumerate(str_):
        try:
            if not (str_[abs(index-1)] == '7' == str_[abs(index+1)] and n == '9'):
                s += n
        except:
            s+=n
    return s