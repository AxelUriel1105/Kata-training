"""Create function fib that returns n'th element of Fibonacci sequence (classic programming task).

"""
def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    fib1, fib2 = 0,1
    for _ in range(2,n+1):
        next = fib1+fib2
        fib1,fib2 = fib2, next
    return fib2