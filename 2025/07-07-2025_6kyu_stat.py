"""You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

"01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  or ,.

To compare the results of the teams you are asked for giving three statistics; range, average and median.

Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

Your task is to return a string giving these 3 values. For the example given above, the string result will be

"Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

where hh, mm, ss are integers (represented by strings) with each 2 digits.

Remarks:
if a result in seconds is ab.xy... it will be given truncated as ab.
if the given string is "" you will return ""
"""
def stat(strg):
    if not strg: return ''
    split_string = strg.split(', ')
    sorted_string = sorted(map(lambda x: x.split('|'),split_string), key=lambda x: (int(x[0]),int(x[1]),int(x[2])))

    return f'Range: {range(sorted_string)} Average: {average(sorted_string)} Median: {median(sorted_string)}'
def range(sorted_string):
    min_h, min_m, min_s = map(int,sorted_string[0])
    max_h, max_m, max_s = map(int,sorted_string[-1])
    minutes = (max_m-min_m)%60-(0,1)[max_s-min_s<0]
    return f'{(max_h-min_h)%24-(0,1)[max_m-min_m<0]:02}|{minutes:02}|{(max_s-min_s)%60:02}'

def average(strg):
    int_list = [list(map(int,l)) for l in strg]
    total_seconds = sum(h*3600+m*60+s for (h,m,s) in int_list)//len(strg)
    print(int_list)
    print(total_seconds)
    return f'{total_seconds//3600:02}|{(total_seconds%3600)//60:02}|{total_seconds%3600%60:02}'

def median(sorted_string):
    med = list(map(int,sorted_string[len(sorted_string)//2]))
    if len(sorted_string)%2!=0:
        return f'{med[0]:02}|{med[1]:02}|{med[2]:02}'
    med2 = list(map(int,sorted_string[len(sorted_string)//2 - 1]))
    return average([med,med2])
