n = 2
m = 3
from random import seed 
from random import randint
seed(123)
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = randint(0, 20)
    print(a[i])

at=[]
print(len(a[0]))
for i in range(len(a[0])):
    at.append([0]*len(a))
    for j in range(len(a)):
        at[i][j]=0
    print(at[i])

for i in range(n):
    for j in range(m):
        a[i][j] = randint(0, 20)
        for o in range():