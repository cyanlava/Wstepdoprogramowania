liczba = int(input("Podaj bok trojkata"))

for i in range(liczba):
    k = i + 1
    w = liczba - k
    print(" " * w + "x" * k)
