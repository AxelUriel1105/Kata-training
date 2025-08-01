"""Implement a function which filters out array values which satisfy the given predicate.

reject([1, 2, 3, 4, 5, 6], lambda x: x % 2 == 0)  =>  [1, 3, 5]

"""
def reject(seq, predicate): 
    return [i for i in seq if not predicate(i)]