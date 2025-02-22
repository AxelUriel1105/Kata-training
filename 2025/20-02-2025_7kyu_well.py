"""For every good kata idea there seem to be quite a few bad ones!

In this kata you need to check the provided 2 dimensional array (x) for good ideas 'good' and bad ideas 'bad'. If there are one or two good ideas, return 'Publish!', if there are more than 2 return 'I smell a series!'. If there are no good ideas, as is often the case, return 'Fail!'.

The sub arrays may not be the same length.

The solution should be case insensitive (ie good, GOOD and gOOd all count as a good idea). All inputs may not be strings."""
def well(arr):
    good_ideas_count = 0
    for ideas_arr in arr:
        good_ideas_count += list(map(lambda x: x.lower() if not str(x).isdigit() else x,ideas_arr)).count('good')
    return {good_ideas_count>2:'I smell a series!',
            0 < good_ideas_count <= 2: 'Publish!' 
           }.get(True, 'Fail!')   