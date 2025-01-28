"""The aim of this kata is to split a given string into different strings
 of equal size (note size of strings is passed to the method)

Example:

Split the below string into other strings of size #3

'supercalifragilisticexpialidocious'

Will return a new string
'sup erc ali fra gil ist ice xpi ali doc iou s'
Assumptions:

String length is always greater than 0
String has no spaces
Size is always positive"""
def split_in_parts(s, part_length):
    split_list = []
    for letter, chunk in zip(s, range(part_length,len(s)+1,part_length)):
        split_list.append(s[chunk- part_length: chunk])
        if len(s[chunk::]) < part_length and s[chunk::]:
            split_list.append(s[chunk::])
    return ' '.join(split_list) if split_list else s