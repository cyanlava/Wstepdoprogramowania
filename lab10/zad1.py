import random 

import time
start = time.time()



list=[]
for i in range(1, 10001):
    list.append(random.randint(0,100))


def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
    return lista            
            
bubble_sort(list)
print(list)
end = time.time()
print(end-start)

#100 liczb - 0.0029921531677246094s
#1000 liczb - 0.09574007987976074s
#10'000 liczb - 8.172135591506958s
