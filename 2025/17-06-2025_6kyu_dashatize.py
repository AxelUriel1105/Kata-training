"""Given an integer, return a string with dash '-' marks before and after each odd digit, but do not begin or end the string with a dash mark.

Ex:

274 -> '2-7-4'
6815 -> '68-1-5'"""
def dashatize(n):
    n = abs(n)
    dashatized_str = str(n)[0] if int(str(n)[0])%2==0 else str(n)[0]+'-'
    for i in str(n)[1::]:
        if dashatized_str[-1] == '-' and int(i)%2!=0:
            dashatized_str+= i + '-'
        elif int(i)%2!=0:
            dashatized_str+= '-' + i + '-'
        else:
            dashatized_str += i
    return dashatized_str if dashatized_str[-1] != '-' else dashatized_str[:-1]