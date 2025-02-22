"""Convert a hash into an array. Nothing more, Nothing less.

{name: 'Jeremy', age: 24, role: 'Software Engineer'}
should be converted into

[["age", 24], ["name", "Jeremy"], ["role", "Software Engineer"]]
Good Luck!"""
def convert_hash_to_array(dct):
    return list(map(list,dct.items()))