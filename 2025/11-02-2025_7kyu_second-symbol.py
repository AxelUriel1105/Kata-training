"""In this kata, you need to write a function that takes a string and a letter as input and then returns the index of the second occurrence of that letter in the string. If there is no such letter in the string, or if the letter occurs only once in the string, -1 should be returned.

Examples:

for inputs  "Hello world!!!", 'l'  ->  return 3
for inputs  "Hello world!!!", 'A'  ->  return -1
Good luck ;) And don't forget to rate this kata if you liked it."""
def second_symbol(s, symbol):
    if symbol not in s or s.count(symbol) == 1:
        return -1
    return s.index(symbol,s.index(symbol)+1)