x = input("podaj wysokosc i szerokosc prostokata:")
m = x.split(" ")
h = int(m[0])
w = int(m[1])


for i in range(0, h):
    n = []
    for i in range(0, w):
        n.append("x")

    string = ""

    l = str(n)
    for i in n:
        string=string+i

    print(string)

