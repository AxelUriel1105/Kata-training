"""When provided with a letter, return its position in the alphabet.

Input :: "a"

Ouput :: "Position of alphabet: 1"

"""
def position(alphabet):
    return "Position of alphabet: {}".format(ord(alphabet)-96)