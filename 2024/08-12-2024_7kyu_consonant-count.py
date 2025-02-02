"""Complete the function that takes a string of English-language text and returns the number of consonants in the string.

Consonants are all letters used to write English excluding the vowels a, e, i, o, u."""
def consonant_count(s):
    return sum(1 for l in s if l.lower() not in 'aeiou' and l.isalpha())