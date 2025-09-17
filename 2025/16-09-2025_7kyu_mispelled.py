"""
Create a function mispelled(word1, word2):

mispelled('versed', 'xersed') # returns True
mispelled('versed', 'applb') # returns False
mispelled('versed', 'v5rsed') # returns True
mispelled('1versed', 'versed') # returns True
mispelled('versed', 'versed') #returns True 
It checks if the word2 differs from word1 by at most one character.

This can include an extra char at the end or the beginning of either of words.

In the tests that expect true, the mispelled word will always differ mostly by one character. 
If the two words are the same, return True
"""
def mispelled(word1,word2):
    if word1 == word2: return True
    if abs(len(word1)-len(word2)) == 1:
        set1 = set(word1) if len(word1) > len(word2) else set(word2)
        set2 = set(word1) if len(word1) < len(word2) else set(word2)
        return len(set1- set2) <= 1
    elif abs(len(word1)-len(word2)) >= 2: return False
    if word1 == '' or word2 == '':
        print('is none')
        if len(word1)<=1 and len(word2)<=1:
            return True
        return False
    word1, word2 = list(word1),list(word2)
    different = next(i for i,(c1,c2) in enumerate(zip(word1,word2)) if c1!=c2)
    word1[different] = word2[different]
    return word1==word2
        
    