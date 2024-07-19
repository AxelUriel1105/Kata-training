"""Longest Palindrome
Find the length of the longest substring in the given string s that is the same in reverse.

As an example, if the input was “I like racecars that go fast”, the substring (racecar) length would be 7.

If the length of the input string is 0, the return value must be 0.

Example:
"a" -> 1 
"aab" -> 2  
"abcde" -> 1
"zzbaabcd" -> 4
"" -> 0
"""

def longest_palindrome (s):
    if not s:
        return 0
    cont = []
    for index,letter in enumerate(s):
        try:
            cut_str = s[index:s.index(letter,index+1)+1]
            if  cut_str == cut_str[::-1]:
                cont.append(len(cut_str))
                if s[index] == s[index+1] == s[index+2]:
                    cont.append(3)
        except:
            pass
    return max(cont) if cont else 1
print('sss')