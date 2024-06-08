"""Definition
A number is called Automorphic number if and only if its square ends in the same digits as the number itself.

Task
Given a number determine if it Automorphic or not ."""
def automorphic(n):
    return "Automorphic" if str(n) in str(n**2)[-len(str(n))::]  else "Not!!"