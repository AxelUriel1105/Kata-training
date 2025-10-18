"""In this kata, you will write an arithmetic list which is basically a list that contains consecutive terms in the sequence.
You will be given three parameters :

first the first term in the sequence
c the constant that you are going to ADD ( since it is an arithmetic sequence...)
l the number of terms that should be returned
Useful link: Sequence

Be sure to check out my Arithmetic sequence Kata first ;)
Don't forget about the indexing pitfall ;)

"""
def seqlist(first, c, l):
    last = first+c*(l-1)
    return list(range(first,(last+1,last-1)[c<0],c))