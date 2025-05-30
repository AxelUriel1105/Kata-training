"""    Your job is to write a function which increments a string, to create a new string.

If the string already ends with a number, the number should be incremented by 1.
If the string does not end with a number. the number 1 should be appended to the new string.
Examples:

foo -> foo1

foobar23 -> foobar24

foo0042 -> foo0043

foo9 -> foo10

foo099 -> foo100

Attention: If the number has leading zeros the amount of digits should be considered.

"""
def increment_string(strng):
    if strng.isalpha() or not strng: return strng + '1'
    try:
        index_last_no_num = next(index for index, chr in enumerate(strng[::-1]) if not chr.isdigit())
        num_strng,alphabetic_strng = strng[-index_last_no_num:], strng[:-index_last_no_num]
        last_strng = 0
        len_num_string = len(num_strng)
        num = f"{int(num_strng) + 1:0{len_num_string}}"
        return alphabetic_strng + num
    except:
        return f"{int(strng) + 1:0{len(strng)}}"