import math
lista = [5, math.pow(5, 2), math.pow(5,3), math.pow(5, 4), math.pow(5, 5), math.pow(5, 6)]
print(lista)

#dodanie
lista.append(math.pow(5, 7))
print(lista)

#długość listy
print(len(lista))

#od drugiej do czwartej
print(lista[1:4])

#od pierwszej do przedostatniej
print(lista[:-1])