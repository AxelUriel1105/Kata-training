"""Write a function that returns a string in which firstname is 
wapped with last name.

Example(Input --> Output)

"john McClane" --> "McClane john"""
def name_shuffler(str_):
    return " ".join(reversed(str_.split()))