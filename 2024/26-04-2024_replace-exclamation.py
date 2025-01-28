"""Description:
Replace all vowel to exclamation mark in the sentence. aeiouAEIOU is vowel.

Examples
replace("Hi!") === "H!!"
replace("!Hi! Hi!") === "!H!! H!!"
replace("aeiou") === "!!!!!"
replace("ABCDE") === "!BCD!"
"""
def replace_exclamation(st):
    return ''.join('!' if chr.upper() in 'AEIOU' else chr for chr in st)