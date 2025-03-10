"""Impliment the reverse function, which takes in input n and reverses it. For instance, reverse(123) should return 321. You should do this without converting the inputted number into a string.

# Please do not use anything from the following list:
['encode','decode','join','zfill','codecs','chr','bytes','ascii', 'substitute','template','bin', 'os','sys','re', '"', "'", 'str','repr', '%s', 'format', 'type', '__', '.keys','eval','exec','subprocess']
            
RecursionFundamentals"""
def reverse(n):
    try:
        reversed = 0
        while n>0:
            last_digit = n%10
            reversed = (reversed*10) + last_digit
            n = n//10
        return reversed
    except:
        return n[::-1]