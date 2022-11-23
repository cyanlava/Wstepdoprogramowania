def rysujlabirynt(macierz, puste, sciana, ludzik, drzwi):
    import numpy
    A = macierz

    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 0:
                A[i][j] = puste
            elif A[i][j] == 1:
                A[i][j] = sciana
            elif A[i][j] == 2:
                A[i][j] = ludzik
            elif A[i][j] == 3:
                A[i][j] = drzwi

    a = numpy.array(A)

    print(a)
 



def aktualizujlabirynt(macierz, ruch):
    import numpy
    rysujlabirynt(macierz, ' ', '#', 'O', 'X')
    sum = 0
    print("sterowanie: w do góry, s do dołu, a w lewo, d w prawo")
    print("przejdz postacia (2) do wyjscia(3)")
    
    a = numpy.array(macierz)
    i = ruch
    #pozycja gracza
    x=1
    y=1
    a[x,y] = 2
    ruch = input("twój ruch ")
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
    if a[5, 5] == 2:
        print('Wygrana!')
        wygrana = 1
        return wygrana
        


def gra(macierz, n):
    rysujlabirynt(macierz, ' ', '#', 'o', 'x')
    sum=0
    while True:
        print("liczba pozostałych ruchów: ", n - sum)
        aktualizujlabirynt(macierz, input('ruch '))
        sum+=1
        if sum == n:
            print("game over")
            break
        if aktualizujlabirynt(macierz, input('ruch ')) == 1:
            break

gra([[1, 1, 1, 1, 1, 1, 1], 
    [1, 2, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 1]], 20)