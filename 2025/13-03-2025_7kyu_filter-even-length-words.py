"""Given an array of strings, write a function that returns an array containing only the elements of the given array whose length is an even number.

Example
["One", "Two", "Three", "Four"] --> ["Four"]"""
def filter_even_length_words(words):
    return list(filter(lambda x: len(x)%2 == 0, words))