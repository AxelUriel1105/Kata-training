"""Given a string and an array of indices, rearrange the characters of the string so that each character is placed at the position specified by the corresponding index in the array.

Examples
Input: 'abcd', [0, 3, 1, 2]

Output: 'acdb'

Explanation:

The character 'a' is placed at index 0.

The character 'b' is placed at index 3.

The character 'c' is placed at index 1.

The character 'd' is placed at index 2.

Notes
The string and the array will always be of equal length.

Both the string and the array will contain valid characters (A-Z, a-z, or 0-9).

"""
def scramble(strng, array):
    sorted_arr= sorted(list(zip(array,strng)),key=lambda x: x[0])
    return ''.join(c[1] for c in sorted_arr)