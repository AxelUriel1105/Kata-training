"""Description:
Remove all exclamation marks from sentence except at the end.

Examples
"Hi!"     ---> "Hi!"
"Hi!!!"   ---> "Hi!!!"
"!Hi"     ---> "Hi"
"!Hi!"    ---> "Hi!"
"Hi! Hi!" ---> "Hi Hi!"
"Hi"      ---> "Hi"
"""
import re
def remove(s):
    pattern = re.compile(r'.+?[a-zA-Z]')
    count_end_exclamations = pattern.match(s[::-1]).group().count('!')
    return s.replace('!','')+'!'*count_end_exclamations if s[-1] == '!' else s.replace('!','')
    