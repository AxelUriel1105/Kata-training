"""Write Number in Expanded Form - Part 2
This is version 2 of my 'Write Number in Exanded Form' Kata.

You will be given a number and you will need to return it as a string in expanded form :

expanded form illustration

For example:

807.304 --> "800 + 7 + 3/10 + 4/1000"
  1.24  --> "1 + 2/10 + 4/100"
  7.304 --> "7 + 3/10 + 4/1000"
  0.04  --> "4/100"
  """
def expanded_form(num):
    integer, decimal = str(num).split('.')
    expanded_int = [str(int(i)*(10**mul)) for i,mul in zip(integer,range(len(integer)-1,-1,-1)) if i!='0']
    expanded_dec = [f'{d}/{10**pow}' for d,pow in zip(decimal,range(1,len(decimal)+1)) if d!='0']
    return ' + '.join(expanded_int + expanded_dec)