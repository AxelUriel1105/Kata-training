"""Write a function that flattens an Array of Array objects into a flat Array. Your function must only do one level of flattening.

flatten [1,2,3] # => [1,2,3]
flatten [[1,2,3],["a","b","c"],[1,2,3]]  # => [1,2,3,"a","b","c",1,2,3]
flatten [[[1,2,3]]] # => [[1,2,3]]"""
def flatten(lst):
    flatten_list = []
    for i in lst:
        if isinstance(i,list):
            flatten_list+=i
        else:
            flatten_list.append(i)
    return flatten_list