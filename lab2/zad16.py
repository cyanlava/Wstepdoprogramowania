from re import A


x = 123

if x > 99:
    a = x % 100 
    b = a % 10
    #cyfra setek
    s = (x - a)/100
    print("cyfra setek:", s)
    #cyfra dziesiątek
    d = (a - b)/10
    print("cyfra dziesiątek:", d)
    #cyfra jedności
    print("cyfra jednoości: ", b)
    

    
else: 
    print("potrzebna liczba większa od 99")