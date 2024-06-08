"""You will be given a number and you will need to return it as a
 string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'"""
def expanded_form(num):
    stringNum = str(num)
    sizeNum = len(stringNum)
    containerInit = sizeNum
    listNum = []

    for i in range(0,sizeNum):
        if stringNum[i] + (containerInit-1)*"0" != "0"+ (containerInit-1)*"0":
            listNum.append(stringNum[i] + (containerInit-1)*"0")
        containerInit-=1
    return " + ".join(listNum)