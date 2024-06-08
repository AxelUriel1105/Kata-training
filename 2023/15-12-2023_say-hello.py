"""a person. Note that name will be an array consisting of one or more values that 
should be joined together with one space between each, and the length of the name array 
in test cases will vary.

Example:

['John', 'Smith'], 'Phoenix', 'Arizona'
This example will return the string Hello, John Smith! Welcome to Phoenix, Arizona!

"""
def say_hello(name, city, state):
    complete_name = " ".join(name)
    return f"Hello, {complete_name}! Welcome to {city}, {state}!"