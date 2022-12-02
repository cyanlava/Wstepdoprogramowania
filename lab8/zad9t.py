

def factorize(n):
    if n > 2:
        i = 1
        for i in range(2, n+1):
            if n%i != 0:
                i+=1
            else:
                if n/i >= 1:
                    print(i)
                    factorize(int(n/i))
                    break    
                


factorize(676)