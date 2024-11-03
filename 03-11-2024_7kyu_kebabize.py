"""Modify the kebabize function so that it converts a camel case string into a kebab case.

"camelsHaveThreeHumps"  -->  "camels-have-three-humps"
"camelsHave3Humps"  -->  "camels-have-humps"
"CAMEL"  -->  "c-a-m-e-l"
Notes:

the returned string should only contain lowercase letters"""
def kebabize(st):
    st = (s for s in st if s.isalpha())
    return ''.join(' ' + s.lower() if s.isupper() else s for s in st).strip().replace(' ','-')