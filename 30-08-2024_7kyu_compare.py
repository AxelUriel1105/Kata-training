"""Compare two strings by comparing the sum of their values (ASCII character code).

For comparing treat all letters as UpperCase
null/NULL/Nil/None should be treated as empty strings
If the string contains other characters than letters, treat the whole string as it would be empty
Your method should return true, if the strings are equal and false if they are not equal.

Examples:
"AD", "BC"  -> equal
"AD", "DD"  -> not equal
"gf", "FG"  -> equal
"zz1", ""   -> equal (both are considered empty)
"ZzZz", "ffPFF" -> equal
"kl", "lz"  -> not equal
null, ""    -> equal"""
def compare(s1, s2):
    s1 = (s1, '1')[s1 in ('', None)]
    s2 = (s2, '1')[s2 in ('', None)]
    check_s1 = all(i.isalpha() for i in s1)
    check_s2 = all(i.isalpha() for i in s2)
    return ('', sum(map(ord,s1.upper())))[check_s1] == ('', sum(map(ord,s2.upper())))[check_s2]
