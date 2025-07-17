"""Challenge:
Given two strings string and prefix, return whether string starts with prefix, as a boolean.

Example:
// string        prefix
"hello world!", "hello"    => true
"hello world!", "HELLO"    => false
"nowai",        "nowaisir" => false
Addendum:
For this problem, an empty prefix string should always return true for any value of string.

If the length of the prefix string is greater than the length of the string, return false.

The check should be case-sensitive, i.e. "hello", "HE" should return false, whereas "hello", "he" should return true.

No characters should be ignored and/or omitted during the test, e.g. whitespace characters should not be ignored."""
def starts_with(st, prefix): 
    return st.startswith(prefix)