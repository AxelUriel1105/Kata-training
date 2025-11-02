"""Here you have to do some mathematical operations on a "dirty string". This kata checks some basics, it's not too difficult.

So what to do?

Input: String which consists of two positive numbers (doubles) and exactly one operator like +, -, * or / always between these numbers. The string is dirty, which means that there are different characters inside too, not only numbers and the operator. You have to combine all digits left and right, perhaps with "." inside (doubles), and to calculate the result which has to be rounded to an integer and converted to a string at the end.

Easy example:
Input: "gdfgdf234dg54gf*23oP42"
Output: "54929268" (because 23454*2342=54929268)
First there are some static tests, later on random tests too...

Hope you have fun! :-)
"""
def calculate_string(st): 
    add, substract, by, divide = lambda x,y: x+y, lambda x,y: x-y, lambda x,y: x*y, lambda x,y: x/y
    operator = {
        '+' in st:('+', add),
        '-' in st:('-', substract),
        '*' in st:('*',by),
        '/' in st:('/', divide)
    }.get(True)
    left_numbers, right_numbers = st.split(operator[0])
    left_numbers = float(''.join(filter(lambda x: x.isdigit() or x=='.', left_numbers)))
    right_numbers = float(''.join(filter(lambda x: x.isdigit() or x=='.', right_numbers)))
    result = operator[1](left_numbers, right_numbers)
    return str(round(result))