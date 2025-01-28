"""An anagram is the result of rearranging the letters of 
a word to produce a new word (see wikipedia).

Note: anagrams are case insensitive

Complete the function to return true if the two arguments given 
are anagrams of each other; return false otherwise.

Examples
"foefet" is an anagram of "toffee"

"Buckethead" is an anagram of "DeathCubeK"

"""
from collections import Counter
def is_anagram(test, original):
    test = test.lower()
    original = original.lower()
    if len(test) != len(original):
        return False
    originalDict = Counter(original)
    testBool = [True if test.count(i) == originalDict.get(i) else False for i in test]
    return all(testBool)