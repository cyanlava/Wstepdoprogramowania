import math
a = 2
b = 1
c = 1

delta = math.pow(b, 2) - 4 * a * c

print(delta)

if a == 0 and b == 0 and c == 0:
    print("nieskończona ilość rozwiązań")

elif a == 0 and b != 0:
    x = - c/b
    print("Podana fukcja jest liniowa, i ma tylko jedno rozwiązanie: ", x)

elif delta == 0:
    if a == 0 and b == 0:
        print("zachodzi nieprawidłowość - 0 musi być równe 0")
    else:
        x = - b / 2 * a
        print("Funkcja kwadratowa ma jedno rozwiązanie: ", x)

elif delta > 0:
    xjeden = (-b - math.sqrt(delta))/ 2 * a
    xdwa = (-b + math.sqrt(delta))/ 2 * a
    print("Funkcja ma dwa rozwiązania: ", xjeden, "oraz ", xdwa)

elif delta < 0:
    print("Funkcja o danych parametrach nie ma miejsc zerowych")

    
