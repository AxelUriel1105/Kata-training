"""ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters after 
it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13. If there are numbers 
or special characters included in the string, they should be returned as they are. Only letters from the
 latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating."""
import string
def rot13(s):
    enum_alphabet = dict(enumerate(string.ascii_lowercase))
    cipher_list = []
    for i in s:
        if i.isalpha() and i != ' ':
            get_n = ord(i.lower()) - 97
            is_upper = i.isupper()
            if get_n > 12:
                cipher_letter = enum_alphabet.get(get_n % 13)
                cipher_letter_case = (cipher_letter,cipher_letter.upper())[is_upper]
                cipher_list.append(cipher_letter_case)
            elif get_n >= 0:
                cipher_letter = enum_alphabet.get(get_n + 13)
                cipher_letter_case = (cipher_letter,cipher_letter.upper())[is_upper]
                cipher_list.append(cipher_letter_case)
        else:
            cipher_list.append(i)
    return ''.join(cipher_list)