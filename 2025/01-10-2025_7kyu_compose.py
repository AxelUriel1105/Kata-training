"""A squared string is a string of n lines, each substring being n characters long. We are given two n-squared strings.

For example:

s1 = "abcd\nefgh\nijkl\nmnop"

s2 = "qrst\nuvwx\nyz12\n3456"

Let us build a new string strng of size (n + 1) x n in the following way:

The first line of strng has the first char of the first line of s1 plus the chars of the last line of s2.
The second line of strng has the first two chars of the second line of s1 plus the chars of the penultimate line of s2 except the last char
and so on until the nth line of strng has the n chars of the nth line of s1 plus the first char of the first line of s2.
So we have:

strng --> "a3456\nefyz1\nijkuv\nmnopq"

or printed:
abcd    qrst  -->  a3456
efgh    uvwx       efyz1
ijkl    yz12       ijkuv
mnop    3456       mnopq"""
def compose(s1, s2):
    s1_split, s2_split = s1.split('\n'), s2.split('\n')[::-1]
    cut_s1 = [s[:index] for index,s in enumerate(s1_split,1)]
    cut_s2 = [s[:len(s2_split[0])-index] for index,s in enumerate(s2_split)]
    return '\n'.join(slice_1 + slice_2 for slice_1,slice_2 in zip(cut_s1,cut_s2))