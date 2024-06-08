"""Write a simple regex to validate a username. Allowed characters are:

lowercase letters,
numbers,
underscore
Length should be between 4 and 16 characters (both included).

"""
def validate_usr(username):
    return all((i.islower() or i.isdigit() or i == '_' for i in username)) and 4 <= len(username) <= 16