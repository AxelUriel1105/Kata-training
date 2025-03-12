"""A balanced number is a number where the sum of digits to the left of the middle digit(s) and the sum of digits to the right of the middle digit(s) are equal.

If the number has an odd number of digits, then there is only one middle digit. (For example, 92645 has one middle digit, 6.) Otherwise, there are two middle digits. (For example, the middle digits of 1301 are 3 and 0.)

The middle digit(s) should not be considered when determining whether a number is balanced or not, e.g. 413023 is a balanced number because the left sum and right sum are both 5."""
def balanced_num(number):
    middle = len(str(number))//2
    if len(str(number)) <= 2: return 'Balanced'
    elif len(str(number))%2 == 0:
        left, right = str(number)[:middle-1],str(number)[middle+1:]
        print(left,right)
        return ('Not Balanced','Balanced')[sum(int(n) for n in left) == sum(int(n) for n in right)]
    else:
        print(number)
        left, right = str(number)[:middle],str(number)[middle+1:]
        return ('Not Balanced','Balanced')[sum(int(n) for n in left) == sum(int(n) for n in right)]