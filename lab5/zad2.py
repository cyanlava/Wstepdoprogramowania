A = [[1, 2, 3], [4, 5, 6]]
B = [[10, 11], [20, 21], [30, 31]]

#wymiary matryc
w1 = len(A) #wiersze
k1 = len(A[0]) #kolumny

w2 = len(B) #wiersze
k2 = len(B[0]) #kolumny



wynik = []
for i in range(w1):
    wynik.append([0] * k2)
    for j in range(k2):
        wynik[i][j] = 0

for i in range(w1):
    for j in range(k2):
        for k in range(w2):
            wynik[i][j] += A[i][k] * B[k][j]
   

for i in range(w1):
    print(A[i])

for i in range(w2):
    print(B[i])

for i in range(w1):
    print(wynik[i])