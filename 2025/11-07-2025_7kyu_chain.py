"""Write a generic function chainer
Write a generic function chainer that takes a starting value, and an array of functions to execute on it (array of symbols for Ruby).

The input for each function is the output of the previous function (except the first function, which takes the starting value as its input). Return the final value after execution is complete.

def add10(x): return x + 10
def mul30(x): return x * 30

chain(50, [add10, mul30])
# returns 1800"""
def chain(init_val, functions):
    if functions:
        x = functions[0](init_val)
        if len(functions) == 1: return x
        for f in functions[1::]:
            x = f(x)
        return x
    return init_val   

    