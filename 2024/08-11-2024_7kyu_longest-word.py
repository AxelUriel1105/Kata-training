"""Given a string of space separated words, return the longest word.
If there are multiple longest words, return the rightmost longest word.

Examples
"red white blue"  =>  "white"
"red blue gold"   =>  "gold"
"""
def longest_word(string_of_words):
    length = list(map(len, string_of_words.split()))[::-1]
    return string_of_words.split()[::-1][length.index(max(length))]