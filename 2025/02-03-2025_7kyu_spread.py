"""You must create a function, spread, that takes a function and a list of arguments to be applied to that function. You must make this function return the result of calling the given function/lambda with the given arguments.

eg:

spread(someFunction, [1, true, "Foo", "bar"] ) 
# is the same as...
someFunction(1, true, "Foo", "bar")
"""
from functools import reduce
def spread(func, args):
    try:
        a,b = reduce(func,args)
        return (a[0],a[1],b) 
    except:
        return reduce(func,args)