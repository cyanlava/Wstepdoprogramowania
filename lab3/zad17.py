n = 0

for j in range(2, 101):
    m = []
    
    for i in range(2, j):
        if j % i == 0:
            m.append(i)



    if len(m) == 0:
        print(j)
        n = n + 1

print("liczb pierwszych w zakresie jest: ", n)
        

    