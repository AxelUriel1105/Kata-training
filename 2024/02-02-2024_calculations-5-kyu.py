"""This time we want to write calculations using functions and get the results. Let's have a look at some examples:

seven(times(five())) # must return 35
four(plus(nine())) # must return 13
eight(minus(three())) # must return 5
six(divided_by(two())) # must return 3
Requirements:

There must be a function for each number from 0 ("zero") to 9 ("nine")
There must be a function for each of the following mathematical operations: plus, minus, times, divided_by
Each calculation consist of exactly one operation and two numbers
The most outer function represents the left operand, the most inner function represents the right operand
Division should be integer division. For example, this should return 2, not 2.666666...:
eight(divided_by(three()))"""
def zero(num = 0): return int(eval(f'{0}{num}')) if num != 0 else 0
def one(num = 0): return int(eval(f'{1}{num}')) if num != 0 else 1
def two(num = 0): return int(eval(f'{2}{num}')) if num != 0 else 2
def three(num = 0): return int(eval(f'{3}{num}')) if num != 0 else 3
def four(num = 0): return int(eval(f'{4}{num}')) if num != 0 else 4
def five(num = 0): return int(eval(f'{5}{num}')) if num != 0 else 5
def six(num = 0): return int(eval(f'{6}{num}')) if num != 0 else 6
def seven(num = 0): return int(eval(f'{7}{num}')) if num!= 0 else 7
def eight(num = 0): return int(eval(f'{8}{num}')) if num != 0 else 8
def nine(num = 0): return int(eval(f'{9}{num}')) if num != 0 else 9

def plus(a): return f'+{a}' 
def minus(a): return f'-{a}'
def times(a): return f'*{a}'
def divided_by(a): return f'/{a}'