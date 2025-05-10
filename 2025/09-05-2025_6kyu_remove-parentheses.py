"""Remove the parentheses
In this kata you are given a string for example:

"example(unwanted thing)example"
Your task is to remove everything inside the parentheses as well as the parentheses themselves.

The example above would return:

"exampleexample"
Notes
Other than parentheses only letters and spaces can occur in the string. Don't worry about other brackets like "[]" and "{}" as these will never appear.
There can be multiple parentheses.
The parentheses can be nested.
"""
def remove_parentheses(st):
    parentheses = 0
    removed_parentheses = ''
    for chr in st:
        if chr == '(':
            parentheses += 1
        if parentheses > 0 and chr == ')':
            parentheses -= 1
            continue
        if parentheses<=0:
            removed_parentheses+=chr
    return removed_parentheses