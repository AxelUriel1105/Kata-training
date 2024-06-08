"""Description:
Remove the minimum number of exclamation marks from the start/end 
of each word in the sentence to make their amount equal on both sides.

Notes:
Words are separated with spaces
Each word will include at least 1 letter
There will be no exclamation marks in the middle of a word
Examples
remove("Hi!") === "Hi"
remove("!Hi! Hi!") === "!Hi! Hi"
remove("!!Hi! !Hi!!") === "!Hi! !Hi!"
remove("!!!!Hi!! !!!!Hi !Hi!!!") === "!!Hi!! Hi !Hi!"""
def remove(s):
    SplitList = s.split(" ")
    SplitExc = s.split("!")
    joinexc = " ".join(SplitExc)
    Text = joinexc.split()
    countExclamLeft = []
    countExclamRight = []
    j = 0
    for i in SplitList:
        countExclamLeft.append(i.find(Text[j][0]))
        countExclamRight.append(i[::-1].find(Text[j][-1]))
        j += 1

    zipList = list(zip(countExclamLeft,countExclamRight))
    lowestNumList = []
    for i in range(0,len(zipList)):
        if zipList[i][0] < zipList[i][1]:
            lowestNumList.append(zipList[i][0])
        else:
            lowestNumList.append(zipList[i][1])

    exclamationList = []
    k = 0
    for i in lowestNumList:
        exclamationList.append("!"*i + Text[k] + "!"*i)
        k += 1


    return " ".join(exclamationList)
