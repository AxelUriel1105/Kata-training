"""he vowel substrings in the word codewarriors are o,e,a,io. The longest of these has a length of 2. Given a lowercase string that has alphabetic characters only (both vowels and consonants) and no spaces, return the length of the longest vowel substring. Vowels are any of aeiou.

Good luck!

If you like substring Katas, please try:

Non-even substrings

Vowel-consonant lexicon"""
def solve(s):
    max_len = vowels = 0
    for l in s:
        if l in 'aeiou':
            vowels += 1
            max_len = max(vowels, max_len)

        else: 
            vowels = 0
    return max_len