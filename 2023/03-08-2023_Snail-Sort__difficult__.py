"""Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, 
traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]"""
def snail(array):
    if array == [[]]:
        return []
    
    sizeArray = len(array)
    InitValue1 = 0
    finalValue1 = sizeArray
    indexInit1 = 0
    InitValue2 = 1
    finalValue2 = sizeArray
    indexInit2 = sizeArray - 1
    InitValue3 = sizeArray -2
    finalValue3 = -1
    indexInit3 = sizeArray -1
    InitValue4 = sizeArray -2
    finalValue4 = 0
    indexInit4 = 0
    cont = 0
    lista = []
    while cont < sizeArray:
        lista.extend([array[indexInit1][i] for i in range(InitValue1,finalValue1)])
        lista.extend([array[i][indexInit2] for i in range(InitValue2,finalValue2)])
        lista.extend([array[indexInit3][i] for i in range(InitValue3,finalValue3,-1)])
        lista.extend([array[i][indexInit4] for i in range (InitValue4,finalValue4,-1)])
        InitValue1 +=1
        InitValue2 +=1
        InitValue3 -= 1
        InitValue4 -= 1
        finalValue1-=1
        finalValue2 -= 1
        finalValue3 += 1
        finalValue4 += 1
        indexInit4 += 1
        indexInit3 -= 1
        indexInit2 -= 1
        indexInit1 += 1

        cont+=1
    return lista
    