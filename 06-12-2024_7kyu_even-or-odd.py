"""Given a string of digits confirm whether the sum of all the individual even digits are greater than the sum of all the indiviudal odd digits. Always a string of numbers will be given.

If the sum of even numbers is greater than the odd numbers return: "Even is greater than Odd"

If the sum of odd numbers is greater than the sum of even numbers return: "Odd is greater than Even"

If the total of both even and odd numbers are identical return: "Even and Odd are the same"

"""
def even_or_odd(s):
    even = sum(int(n) for n in s if int(n)%2==0)
    odd = sum(int(n) for n in s if int(n)%2!=0)
    return {even>odd: 'Even is greater than Odd',
            even<odd: 'Odd is greater than Even'
            }.get(True, "Even and Odd are the same")