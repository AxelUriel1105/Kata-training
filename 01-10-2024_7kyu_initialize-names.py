"""Some people just have a first name; some people have first and last names and some people have first, middle and last names.

You task is to initialize the middle names (if there is any).

Examples
'Jack Ryan'                   => 'Jack Ryan'
'Lois Mary Lane'              => 'Lois M. Lane'
'Dimitri'                     => 'Dimitri'
'Alice Betty Catherine Davis' => 'Alice B. C. Davis'"""
def initialize_names(name):
    list_name = name.split()
    return ' '.join(n if index in (0,len(list_name)-1) else n[0].upper()+'.' for index,n in enumerate(list_name))
