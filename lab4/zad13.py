n = 7
m = 10
from random import seed 
from random import randint
seed(123)
a = []
for i in range(n):
    a.append([randint(0, 20)] * m)
print(a)

for i in a:
    print(i)

a=[randint(0, 20)] * n
for i in range(n):
    a[i] = [randint(0,20)] * m