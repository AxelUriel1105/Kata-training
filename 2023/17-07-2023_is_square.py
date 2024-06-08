"""The tests will always use some integral number, so don't worry about that in dynamic typed languages.

Examples
-1  =>  false
 0  =>  true
 3  =>  false
 4  =>  true
25  =>  true
26  =>  false
"""
def is_square(n):  
    if n>=0:
        i=0
        while i<=n:
            if i*i == n:
                return True
            elif i==n and i*i!=n:
                return False
            else:
                i+=1
                
    else:
        return False

print(is_square(81))