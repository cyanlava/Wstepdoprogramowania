n = 7
m = n
from random import seed 
from random import randint
seed(123)
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = randint(0, 20)
    print(a[i])

o=0
y=0
l = n-1
for i in range(n):
    m = int(a[i][i])
    o = o + m
    for j in range(n-i):
        print(i, l-j)

        x = int(a[i][l-j])
        y=y+x
print(y-o)
    #k = i + 1
   # w = n - k
    #print(" " * w + "x" * k)
