"""Write function replaceAll (Python: replace_all) that will replace all occurrences of an item with another.

Python / JavaScript: The function has to work for strings and lists.

Example: replaceAll [1,2,2] 1 2 -> in list [1,2,2] we replace 1 with 2 to get new list [2,2,2]

replaceAll(replaceAll(array: [1,2,2], old: 1, new: 2) // [2,2,2]
"""
def replace_all(obj, find, replace):
    if isinstance(obj, list):
        return [i if i!=find else replace for i in obj]
    else:
        return obj.replace(find,replace)