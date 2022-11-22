o = 9
n = 0

l = []
while o >= n:
    for j in range(2, o):
        m = []
    
        for i in range(2, j):
            if j % i == 0:
                m.append(i)



        if len(m) == 0:
            l.append(j)
            n = n + 1

print(max(l))

while n>=