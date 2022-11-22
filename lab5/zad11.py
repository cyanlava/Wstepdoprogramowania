import numpy
a = numpy.array([[1, 1, 1, 1, 1, 1, 1], 
[1, 2, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 3, 1],
[1, 1, 1, 1, 1, 1, 1]])



x = 1
y = 1
sum = 0
while True:
    print("sterowanie: w do góry, s do dołu, a w lewo, d w prawo")
    print("przejdz postacia (2) do wyjscia(3)")
    print("liczba pozostałych ruchów: ", 20 - sum)
    print(a)
    #pozycja gracza
    a[x,y]= 2
    i = input("twój ruch ")
    if i == 's' and a[x + 1, y] == 0 or a[x + 1, y] == 3:
        a[x,y] = 0
        a[x+1,y] = 2
        x+=1
    elif i == "w" and a[x - 1, y] == 0 or a[x - 1, y] == 3:
        a[x,y] = 0
        a[x-1,y] = 2
        x-=1
    elif i == 'd' and a[x, y + 1] == 0 or a[x, y + 1] == 3:
        a[x,y] = 0
        a[x, y+1] = 2
        y+=1
    elif i == 'a' and a[x, y - 1] == 0 or a[x, y - 1] == 3:
        a[x, y] = 0
        a[x, y-1] = 2
        y-=1
    sum += 1
    if sum == 20:
        print('game over')
        break
    if a[5,5] == 2:
        print("wygrana!")
        break

