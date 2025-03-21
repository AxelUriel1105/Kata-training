"""A new task for you!

You have to create a method, that corrects a given time string.
There was a problem in addition, so many of the time strings are broken.
Time is formatted using the 24-hour clock, so from 00:00:00 to 23:59:59.
Examples
"09:10:01" -> "09:10:01"  
"11:70:10" -> "12:10:10"  
"19:99:99" -> "20:40:39"  
"24:01:01" -> "00:01:01"  
If the input-string is null or empty return exactly this value! (empty string for C++) If the time-string-format is invalid, return null. (empty string for C++)

Have fun coding it and please don't forget to vote and rank this kata! :-)

I have created other katas. Have a look if you like coding and challenges.

"""
import re
def time_correct(t):
    if not t: return t
    pattern = re.compile(r'(\d{2}):(\d{2}):(\d{2})')
    if not pattern.match(t): return None
    try:
        hours, minutes, seconds = int(t[:2]), int(t[3:5]), int(t[-2:])
        if seconds >= 60:
            minutes += 1
            seconds = seconds%60
        if minutes >= 60:
            hours += 1
            minutes = minutes%60
        return f'{hours%24:02}:{minutes:02}:{seconds:02}'
    except: 
        return None