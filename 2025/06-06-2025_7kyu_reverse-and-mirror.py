"""Given 2 string parameters, show a concatenation of:

the reverse of the 2nd string with inverted case; e.g Fish -> HSIf
a separator in between both strings: @@@
the 1st string reversed with inverted case and then mirrored; e.g Water -> RETAwwATER 
** Keep in mind that this kata was initially designed for Shell, I'm aware it may be easier in other languages.**"""
def reverse_and_mirror(s1, s2):
    return s2.swapcase()[::-1]+'@@@'+s1.swapcase()[::-1]+s1.swapcase()
