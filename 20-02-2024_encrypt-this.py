"""Acknowledgments:
I thank yvonne-liu for the idea and for the example tests :)

Description:
Encrypt this!

You want to create secret messages which can be deciphered by the Decipher this! kata. Here are the conditions:

Your message is a string containing space separated words.
You need to encrypt each word in the message using the following rules:
The first letter must be converted to its ASCII code.
The second letter must be switched with the last letter
Keepin' it simple: There are no special characters in the input.
Examples:
encrypt_this("Hello") == "72olle"
encrypt_this("good") == "103doo"
encrypt_this("hello world") == "104olle 119drlo"
"""
def encrypt_this(text):
    return " ".join(encrypt_word(i) for i in text.split()) if text else ""
    
def encrypt_word(text):
    if len(text) > 2:
        return "{}{}{}{}".format(ord(text[0]),text[-1],text[2:-1],text[1]) 
    elif len(text) == 2:
        return f"{ord(text[0])}{text[-1]}"
    else:
        return str(ord(text[0]))