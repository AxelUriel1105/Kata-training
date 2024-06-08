"""Implement String#digit? (in Java StringUtils.isDigit(String)), which should return 
true if given object is a digit (0-9), false otherwise."""
def is_digit(n):
    return 0 <= int(n) < 10 if n.isdigit() else False 