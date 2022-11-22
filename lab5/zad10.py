x = 156
l=[]
while x>0:
    cyfra = x % 2
    l.append(cyfra)
    x=x//2
l.reverse()
print(l)
