"""Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:

[
  "  *  ",
  " *** ", 
  "*****"
]
And a tower with 6 floors looks like this:

[
  "     *     ", 
  "    ***    ", 
  "   *****   ", 
  "  *******  ", 
  " ********* ", 
  "***********"
]"""
def tower_builder(n_floors):
    supRange = 2 * n_floors
    spaceInit = int((supRange-2)/2)
    treeStars = []

    for i in range (1,supRange,2):
        treeStars.append( spaceInit*" " + i*('*') + spaceInit*" ")
        spaceInit-=1
        
    return treeStars


