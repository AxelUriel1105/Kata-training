"""Basic regex tasks. Write a function that takes in a numeric code 
of any length. The function should check if the code begins with 1, 2, or 3 
nd return true if so. Return false otherwise.

You can assume the input will always be a number.

"""
def validate_code(code):
    return int(str(code)[0]) in (1,2,3)
