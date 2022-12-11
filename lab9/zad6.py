def nwd(a, b):
    while b!=0:
        pom=b
        b=a%b
        a=pom
    return a

#x = nwd(120 ,24)
#print(x)

def nwd_rek(a,b):
    if b!=0:
        return nwd_rek(b,a%b)
    return a

x = nwd_rek(120 ,24)
print(x)