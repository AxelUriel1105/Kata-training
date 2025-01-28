"""Note that the return string must list the letters in order of their first appearance in the original string.

More examples:

"Bangkok"    -->  "b:*,a:*,n:*,g:*,k:**,o:*"
"Las Vegas"  -->  "l:*,a:**,s:**,v:*,e:*,g:*"
Have fun! ;)

"""
from collections import Counter
def get_strings(city):
    n_letters = Counter(city.lower().replace(' ',''))
    return ','.join(f'{l}:{"*"*n_letters.get(l)}' for l in n_letters)