import numpy
print("podaj wymiary matrycy n i m: ")
x = input("pamiętaj by oddzielić liczby spacją :) ")
list = x.split(" ")
n = int(list[0])
m = int(list[1])



from random import seed 
from random import randint
seed(123)

print("wersja podstawowa: ")

#tworzenie podstawowej matrycy a
#wymiary matrycy mozna zmienic dowolnie przez n i m
a = []
for i in range(n):
    a.append([0] * m)
    for j in range(m):
        a[i][j] = randint(0, 20)
    print(a[i])

#transponowana matryca
print(numpy.transpose(a))

A = [[1, 2, 3], [4, 5, 6]]
B = [[10, 11], [20, 21], [30, 31]]

#wymiary matryc
w1 = len(A) #wiersze
k1 = len(A[0]) #kolumny

w2 = len(B) #wiersze
k2 = len(B[0]) #kolumny


C = numpy.matmul(A, B)
print(C)