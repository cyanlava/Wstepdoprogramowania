liczba = int(input("Podaj bok trojkata"))

n = []
for i in range(0, liczba):
    n.append("x")

string = ""

l = str(n)
for i in n:
    string=string+i
    print(string)
