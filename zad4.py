x = input("podaj boki prostokąta a i b:")
m = x.split(" ")
a = int(m[0])
b = int(m[1])

if a > 0 and b > 0:
    print("pole prostokata wynosi ", a * b, " a jego obwód to ", 2*(a+b))

else:
    print("nieprawidlowe dane")