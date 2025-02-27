"""In this kata, your job is to create a class Dictionary which you can add words to and their entries. Example:

>>> d = Dictionary()

>>> d.newentry('Apple', 'A fruit that grows on trees')

>>> print(d.look('Apple'))
A fruit that grows on trees

>>> print(d.look('Banana'))
Can't find entry for Banana"""
class Dictionary():
    def __init__(self):
        self.Dictionary = {}
    def newentry(self, word, definition):
        self.Dictionary[word] = definition
        
    def look(self, key):
        return self.Dictionary.get(key,f"Can't find entry for {key}")
