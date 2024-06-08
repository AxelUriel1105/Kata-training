"""Your task is to write function factorial.

https://en.wikipedia.org/wiki/Factorial

"""
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else: 
        return n * factorial(n-1)