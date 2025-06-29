"""Write a function reverse which reverses a list (or in clojure's case, any list-like data structure)

(the dedicated builtin(s) functionalities are deactivated)

"""

def reverse(lst):
    lst2, length_lst = lst.copy(), len(lst)
    for i in range(length_lst):
        r =lst.pop()
        lst2.append(r)
    
    for i  in range(length_lst):
        lst2.pop(0)
    return lst2