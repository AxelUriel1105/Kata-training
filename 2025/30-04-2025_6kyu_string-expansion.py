"""Given a string that includes alphanumeric characters ("3a4B2d") return the expansion of that string: The numeric values represent the occurrence of each letter preceding that numeric value. There should be no numeric characters in the final string.

Notes
The first occurrence of a numeric value should be the number of times each character behind it is repeated, until the next numeric value appears
If there are multiple consecutive numeric characters, only the last one should be used (ignore the previous ones)
Empty strings should return an empty string.
Your code should be able to work for both lower and capital case letters.

"3D2a5d2f"  -->  "DDDaadddddff"    # basic example: 3 * "D" + 2 * "a" + 5 * "d" + 2 * "f"
"3abc"      -->  "aaabbbccc"       # not "aaabc", nor "abcabcabc"; 3 * "a" + 3 * "b" + 3 * "c"
"3d332f2a"  -->  "dddffaa"         # multiple consecutive digits: 3 * "d" + 2 * "f" + 2 * "a"
"abcde"     -->  "abcde"           # no digits
"1111"      -->  ""                # no characters to repeat
""          -->  ""                # empty string"""
def string_expansion(s):
    s = ''.join(c for index,c in enumerate(s) if c.isalpha() or (c.isdigit() and s[index+1:index+2].isalpha()))
    if not s: return ''
    elif s.isalpha(): return s
    new_s,n= '', 0
    for c1,c2 in zip(s,s[1:]):
        if c1.isdigit():
            n = int(c1)
            new_s+=c1
        elif c1.isalpha() and c2.isalpha():
            new_s+=c1
            new_s+=str(n)
        else:
            new_s+=c1
    new_s+=s[-1]
    initial_string = ''
    if new_s[0].isalpha():
        first_digit_index = next(index for index, c in enumerate(s) if c.isdigit())
        initial_string = s[:first_digit_index]
    return initial_string + ''.join(int(c1)*c2  for c1,c2 in zip(new_s, new_s[1::]) if c1.isdigit())