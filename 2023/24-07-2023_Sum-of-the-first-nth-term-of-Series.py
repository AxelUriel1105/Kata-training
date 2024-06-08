def series_sum(n):
    if n > 0:
        if n == 1:
            return '1.00'
        elif n == 2:
            return str(1 + 1/4)
        else:
            container = 1 + 1/4
            j = 7
            for i in range(3,n+1):
                container += 1/j
                j+=3
            
            return str(round(container,2))
    else:
        return 0