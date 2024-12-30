"""Task
Remove all exclamation marks from the end of words. Words are separated by a single space. There are no exclamation marks within a word.

Examples
remove("Hi!") === "Hi"
remove("Hi!!!") === "Hi"
remove("!Hi") === "!Hi"
remove("!Hi!") === "!Hi"
remove("Hi! Hi!") === "Hi Hi"
remove("!!!Hi !!hi!!! !hi") === "!!!Hi !!hi !hi"
"""
def remove(st):
    return ' '.join(i[:remove_right(i)] for i in st.split())
def remove_right(word):
    for index,i in enumerate(word[::-1]):
        if i.isalpha():
            return len(word) - index
        