"""Given an array arr of strings, complete the function by calculating the total perimeter of all the islands. Each piece of land will be marked with 'X' while the water fields are represented as 'O'. Consider each tile being a perfect 1 x 1 piece of land. Some examples for better visualization:

['XOOXO',
 'XOOXO',
 'OOOXO',
 'XXOXO',
 'OXOOO'] 
which represents:

should return: "Total land perimeter: 24".

Following input:

['XOOO',
 'XOXO',
 'XOXO',
 'OOXX',
 'OOOO']
which represents:

should return: "Total land perimeter: 18"

"""
def land_perimeter(arr):
    neighbours = [number_of_neighbours((r,c),arr) for r in range(len(arr)) for c in range(len(arr[0])) if arr[r][c] == 'X']
    print(neighbours)
    return 'Total land perimeter: {}'.format(sum(4-n for n in neighbours))

def number_of_neighbours(coord, arr):
    neighbours = [(coord[0], coord[1]-1),(coord[0]-1, coord[1]),(coord[0], coord[1]+1),(coord[0]+1, coord[1])]
    count_neighbours = 0
    for r,c in neighbours:
        if r>=0 and c>=0 and r<len(arr) and c<len(arr[0]):
            count_neighbours += int(arr[r][c] == 'X')
    return count_neighbours