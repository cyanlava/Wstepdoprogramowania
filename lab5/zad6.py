x = 19
i = 2
m=[]
while x>i:
    l=[]
    for j in range(2,i):
        if i%j == 0:
            l.append(j)
    if len(l) == 0:
        m.append(i)

    i+=1
print(len(m))
