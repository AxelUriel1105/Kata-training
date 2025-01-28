"""Reverse every other word in a given string, then return the string.
 Throw away any leading or trailing whitespace, while ensuring there is exactly one space between each word. 
 Punctuation marks should be treated as if they are a part of the word in this kata."""
def reverse_alternate(st):
    return ' '.join(word[::-1] if num%2 != 0 else word for num,word in enumerate(st.split()))