n = 7
m = 10
from random import seed 
from random import randint
seed(123)
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = randint(0, 20)
    print(a[i])
