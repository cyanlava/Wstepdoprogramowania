n = 0
pierwsze = []
for j in range(2, 101):
    m = []
    
    for i in range(2, j):
        if j % i == 0:
            m.append(i)



    if len(m) == 0:
        
        pierwsze.append(j)


print(pierwsze)

for i in pierwsze:
    for j in pierwsze:
        if i - j == -2:  
            print(i, j)
        

    