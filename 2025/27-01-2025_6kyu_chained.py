"""Your task is to write a higher order function for chaining together a list of unary functions. In other words, it should return a function that does a left fold on the given functions.

chained([a,b,c,d])(input)
Should yield the same result as

d(c(b(a(input))))
"""
def chained(functions):
    def func(arg):
        f = 0
        for function in functions:
            f = function(arg) 
            arg = f
        return arg
    return func

