"""Task
Create a function that always returns True/true for every item in a given list.
However, if an element is the word 'flick', switch to always returning the opposite boolean value.

Examples
['codewars', 'flick', 'code', 'wars'] ➞ [True, False, False, False]

['flick', 'chocolate', 'adventure', 'sunshine'] ➞ [False, False, False, False]

['bicycle', 'jarmony', 'flick', 'sheep', 'flick'] ➞ [True, True, False, False, True]
Notes"""
def flick_switch(lst, initial_v = True):
    Boolean_list = []
    for s in lst:
        if s == 'flick':
            initial_v = not(initial_v)
        Boolean_list.append(initial_v)
    return Boolean_list
