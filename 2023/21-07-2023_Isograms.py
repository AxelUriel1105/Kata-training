"""An isogram is a word that has no repeating letters, consecutive or non-consecutive.
 Implement a function that determines whether a string that contains only letters is 
 an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true "aba" --> false "moOse" --> false (ignore letter case)

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false"""

def is_isogram(string):
    container = True
    String_list = [i for i in string.upper()]
    for x in String_list:
        count_letters = String_list.count(x)
        if count_letters>= 2:
            return False
            container = False
            break
        else:
            container = True
    if container == True:
        return True
    