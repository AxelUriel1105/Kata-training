"""Numbers ending with zeros are boring.

They might be fun in your world, but not here.

Get rid of them. Only the ending ones.

1450   -> 145
960000 -> 96
1050   -> 105
-1050  -> -105
0      -> 0"""
def no_boring_zeros(n):
    if str(n)[-1] != '0': return n
    for index,i in enumerate(str(n)[::-1]):
        if i!='0' and i.isdigit():
            return int(str(n)[:-index])
    return n