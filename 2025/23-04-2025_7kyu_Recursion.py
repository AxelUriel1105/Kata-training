"""In this Kata, you will be given two positive integers a and b and your task will be to apply the following operations:

i) If a = 0 or b = 0, return [a,b]. Otherwise, go to step (ii);
ii) If a ≥ 2*b, set a = a - 2*b, and repeat step (i). Otherwise, go to step (iii);
iii) If b ≥ 2*a, set b = b - 2*a, and repeat step (i). Otherwise, return [a,b].
a and b will both be lower than 10E8.

More examples in tests cases. Good luck!

Please also try Simple time difference

"""
def solve(a,b):
    return step_one(a,b)  
def step_one(a,b):
    if a == 0 or b == 0:
        return [a,b]
    return step_two(a,b)
def step_two(a,b):
    if a>=2*b:
        a = a%(2*b)
        return step_one(a,b)
    return step_three(a,b)
def step_three(a,b):
    if b>=2*a:
        b = b%(2*a)
        return step_one(a,b)
    return [a,b]
  