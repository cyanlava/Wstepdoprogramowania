import math

a = 3
b = 3 
c = 3 * math.sqrt(2)

if a == 0 or b == 0 or c == 0:
    print("podane boki nie tworzą trójkąta")

elif a < 0 or b < 0 or c < 0:
    print("podane boki nie tworzą trójkąta")


elif a == b == c:
    print("trójkąt jest ostrokątny, równoboczny")

elif a == b or a == c or b == c:
    if max(a,b,c) == a:
        if  a == b * math.sqrt(2):
            print("trójkąt jest równoramienny, prostokątny")
        elif a * a < b * b + c * c:
            print("trójkąt jest równoramienny, ostrokątny")
        elif a * a > b * b + c * c:
            print("trójkąt jest równoramienny, rozwartokątny")
    elif max(a,b,c) == b:
        if b == a * math.sqrt(2):
            print("trójkąt jest równoramienny, prostokątny")
        elif b * b > a * a + c * c:
            print("trójkąt jest równoramienny, rozwartokątny")
        elif b * b < a * a + c * c:
            print("trójkąt jest równoramienny, ostrokątny")
    elif max(a,b,c) == c:
        if c == a * math.sqrt(2):
            print("trójkąt jest równoramienny, prostokątny")
        elif c * c > a * a + b * b:
            print("trójkąt jest równoramienny, rozwartokątny")
        elif c * c < a * a + b * b:
            print("trójkąt jest równoramienny, ostrokątny")

else:
    if max(a,b,c) == a:
        if a * a == b * b + c * c:
            print("trójkąt jest różnoboczny, prostokątny")
        elif a * a > b * b + c * c:
            print("trójkąt jest różnoboczny, rozwartokątny")
        elif a * a < b * b + c * c:
            print("trójkąt jest różnoboczny, ostrokątny")
    elif max(a,b,c) == b:
        if b * b == a * a + c * c:
            print("trójkąt jest różnoboczny, prostokątny")
        elif b * b > a * a + c * c:
            print("trójkąt jest różnoboczny, rozwartokątny")
        elif b * b < a * a + c * c:
            print("trójkąt jest różnoboczny, ostrokątny")
    elif max(a,b,c) == c:
        if c * c == a * a + b * b:
            print("trójkąt jest różnoboczny, prostokątny")
        elif c * c > a * a + b * b:
            print("trójkąt jest różnoboczny, rozwartokątny")
        elif c * c < a * a + b * b:
            print("trójkąt jest różnoboczny, ostrokątny")

