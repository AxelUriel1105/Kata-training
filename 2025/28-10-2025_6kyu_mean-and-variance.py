"""dataand data1 are two strings with rainfall records of a few cities for months from January to December. The records of towns are separated by \n. The name of each town is followed by :.

data and towns can be seen in "Your Test Cases:".

Task:
function: mean(town, strng) should return the average of rainfall for the city town and the strng data or data1 (In R and Julia this function is called avg).
function: variance(town, strng) should return the variance of rainfall for the city town and the strng data or data1.
Examples:
mean("London", data), 51.19(9999999999996) 
variance("London", data), 57.42(833333333374)"""
def separate_months(months):
    list_of_tuples = list(map(lambda x: tuple(x.split()),months.split(',')))
    return dict(list_of_tuples)

def clean_data(data, town):
    list_of_dict = list(map(lambda x: {x[:x.find(':')]: separate_months(x[x.find(':')+1:])}, data.split('\n')))
    to_dictionary = {k:v for dictionary in list_of_dict for k,v in dictionary.items()}
    town_data = to_dictionary[town]
    return list(float(i) for i in town_data.values())

def mean(town, s):
    try:
        values = clean_data(s,town)
        return sum(values)/len(values)
    except: 
        return -1
def variance(town, s):
    try:
        values = clean_data(s,town)
        mean = sum(values)/len(values)
        return sum((n-mean)**2 for n in values)/(len(values))
    except:
        return -1