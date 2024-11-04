"""Each exclamation mark's weight is 2; each question mark's weight is 3. Putting two strings left and right on the balance - are they balanced?

If the left side is more heavy, return "Left"; if the right side is more heavy, return "Right"; if they are balanced, return "Balance".

Examples
"!!", "??"     -->  "Right"
"!??", "?!!"   -->  "Left"
"!?!!", "?!?"  -->  "Left"
"!!???!????", "??!!?!!!!!!!"  -->  "Balance"
"""
def balance(left, right):
    values = {'!':2,'?':3}
    n_left, n_right = sum(values.get(i, 0) for i in left), sum(values.get(i, 0) for i in right)  
    if n_left == n_right:
        return 'Balance'
    return ('Left', 'Right')[n_right>n_left]