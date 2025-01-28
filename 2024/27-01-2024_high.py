"""Given a string of words, you need to find the highest scoring word.

Each letter of a word scores points according to its position in the alphabet: a = 1, b = 2, c = 3 etc.

For example, the score of abad is 8 (1 + 2 + 1 + 4).

You need to return the highest scoring word as a string.

If two words score the same, return the word that appears earliest in the original string.

All letters will be lowercase and all inputs will be valid."""
def high(x):
    tupleList = [wordValue(i) for i in x.split()]
    maxSum = sorted(tupleList)[-1][0]
    for i in tupleList:
        if i[0] == maxSum:
            return i[1]
def wordValue(word):
    return (sum(ord(i)-96 for i in word),word)