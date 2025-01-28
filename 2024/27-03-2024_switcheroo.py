"""Given a string made up of letters a, b, and/or c, switch the position of letters a and b 
(change a to b and vice versa). Leave any incidence of c untouched.

Example:

'acb' --> 'bca'
'aabacbaa' --> 'bbabcabb'
"""
def switcheroo(s):
    switchDict = {'a':'b','b':'a'}
    return "".join(i if i not in switchDict else switchDict.get(i) for i in s)