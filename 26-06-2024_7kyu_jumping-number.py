"""Definition
Jumping number is the number that All adjacent digits in it differ by 1.

Task
Given a number, Find if it is Jumping or not .

Warm-up (Highly recommended)
Playing With Numbers Series
Notes
Number passed is always Positive .

Return the result as String .

The difference between ‘9’ and ‘0’ is not considered as 1 .

All single digit numbers are considered as Jumping numbers.

Input >> Output Examples
jumpingNumber(9) ==> return "Jumping!!"
Explanation:
It's single-digit number
jumpingNumber(79) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(23) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1
jumpingNumber(556847) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(4343456) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1
jumpingNumber(89098) ==> return "Not!!"
Explanation:
Adjacent digits don't differ by 1
jumpingNumber(32) ==> return "Jumping!!"
Explanation:
Adjacent digits differ by 1"""

def jumping_number(number):
    if len(str(number)) == 1: return "Jumping!!"
    for num1,num2 in zip(str(number),str(number)[1::]):
        if abs(int(num1) - int(num2)) != 1:
            return "Not!!"
    return "Jumping!!"

##Otra solución en 2 lineas de código    
"""
def jumping_number(number):
    if len(str(number)) == 1: return "Jumping!!"
    return "Jumping!!" if all(True if abs(int(n1)-int(n2)) == 1 else False for n1,n2 in zip(str(number),str(number)[1::])) else 'Not!!'
"""