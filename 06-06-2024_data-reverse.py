"""A stream of data is received and needs to be reversed.

Each segment is 8 bits long, meaning the order of these segments needs to be reversed, for example:

11111111  00000000  00001111  10101010
 (byte1)   (byte2)   (byte3)   (byte4)
should become:

10101010  00001111  00000000  11111111
 (byte4)   (byte3)   (byte2)   (byte1)
The total number of bits will always be a multiple of 8.

The data is given in an array as such:

[1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,0,1,0,1,0,1,0]
Note: In the C and NASM languages you are given the third parameter 
which is the number of segment blocks.

"""
def data_reverse(data):
    Data_Reversed = []
    list_groups = [data[x*8:y*8] for x,y in enumerate(range(1,len(data)//8 +1))]
    for i in list(reversed(list_groups)):
        Data_Reversed += i
    return Data_Reversed
        
#Solución 2
"""
def data_reverse(data):
    list_groups = reversed([data[x*8:y*8] for x,y in enumerate(range(1,len(data)//8 +1))])
    return sum(list_groups,[])
"""