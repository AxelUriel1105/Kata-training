"""You are given a secret message you need to decipher. Here are the things you
 need to know to decipher it:

For each word:

the second and the last letter is switched (e.g. Hello becomes Holle)
the first letter is replaced by its character code (e.g. H becomes 72)
there are no special characters used, only letters and spaces
words are separated by a single space
there are no leading or trailing spaces
Examples

'72olle 103doo 100ya' --> 'Hello good day'
'82yade 115te 103o'   --> 'Ready set go'"""
def decipher_this(s):
    if s:
        return ' '.join(decrypt_word(word) for word in s.split())
    else: return None

def decrypt_word(s):
    try:
        return chr(int(s))
    except:
        if len(s) == 2:
            return s[::-1]
        elif len(s) == 1: return s
        else:
            num = int(''.join(n for n in s if n.isdigit()))
            s = s.replace(str(num),chr(num))
            characList = list(s)
            secondChr = characList[1]
            characList[1] = characList[-1]
            characList[-1] = secondChr
            return ''.join(characList)