
def bubble_sort(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if(lista[j] > lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                print(i, j, lista)
            else:
                print('nie wieksze', i, j, lista)
    print(lista)

bubble_sort([6, 2, 7, 1, 5])

def bubblesort_min(lista):
    n = len(lista)
    for i in range(n-1):
        for j in range(n-i-1):
            if(lista[j] < lista[j+1]):
                lista[j], lista[j+1] = lista[j+1], lista[j]
                
    return lista

x = bubblesort_min([6, 2, 7, 1, 5,4,1,9,0])
print(x)