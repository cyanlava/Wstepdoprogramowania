def rysujlabirynt(macierz, puste, sciana, ludzik, drzwi):
    
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
        
    



def aktualizujlabirynt(macierz, ruch, gracz, sciana):
    
    print("sterowanie: w do góry, s do dołu, a w lewo, d w prawo")
    print("przejdz postacia", ludzik, "do wyjscia", drzwi)
    
    
    a = macierz
    #pozycja graczas

    i = ruch
    if i == 's' and a[gracz[0] + 1][gracz[1]] != sciana:
        a[gracz[0]][gracz[1]] = puste
        a[gracz[0] + 1][gracz[1]]=ludzik    
        gracz[0]+=1
    elif i == "w" and a[gracz[0] - 1][gracz[1]] != sciana:
        a[gracz[0]][gracz[1]] = puste
        a[gracz[0]-1][gracz[1]] = ludzik
        gracz[0]-=1
    elif i == 'd' and a[gracz[0]][gracz[1] + 1] != sciana:
        a[gracz[0]][gracz[1]] = puste
        a[gracz[0]][gracz[1] + 1] = ludzik
        gracz[1]+=1
    elif i == 'a' and a[gracz[0]][gracz[1]] != sciana:
        a[gracz[0]][gracz[1]] = puste
        a[gracz[0]][gracz[1]] = ludzik
        gracz[1]-=1
    
    
        


def gra(macierz, n, gracz, meta):
    rysujlabirynt(macierz, puste, sciana, ludzik, drzwi)
    sum=0
    for i in range(len(macierz)):
        print(macierz[i])
    
    while True:
        print("liczba pozostałych ruchów: ", n - sum)
        ruch = input('Czas na twoj ruch! :')
        aktualizujlabirynt(macierz, ruch, gracz, sciana)
        sum+=1
        for i in range(len(macierz)):
            print(macierz[i])
        if sum == n:
            x = 'X'
            y = '#'
            print(11*' ',x,x,x,11*' ')
            print(7*' ',x,x,5*' ',x,x,7*' ')
            print(5*' ',x,13*' ',x,5*' ')
            print(3*' ',x,3*' ',y,5 *' ', y, 3*' ', x, 3* ' ')
            print(3* ' ', x, ' ', y,y, 5 *' ',y,y, ' ', x, 3* ' ')
            print( ' ', x, 3*' ', y,y,  5 * ' ',y,y,3*' ', x, ' ')
            print( ' ', x, ' ', y,y,y, 5*' ', y,y,y, ' ', x, ' ')
            print( ' ', x, 9*' ', y, 9* ' ', x, ' ')
            print(3* ' ', x, 5*' ', y, ' ', y, 5 *' ', x, 3* ' ')
            print(3* ' ', x, 5*' ', y, ' ', y, 5 *' ', x, 3* ' ')
            print(5 *' ', x, 13*' ', x, 5* ' ')
            print(7 * ' ', x,x, 5 * ' ', x,x, 7 * ' ')
            print(11 * ' ', x,x,x, 11 * ' ')
            print(9*' ', "GAME OVER")
            break
        
        if gracz == meta:
            x='x'
            y = 'X'
            
            print(11 * ' ', x,x,x, 11 * ' ')
            print(7 * ' ', x,x, 5 * ' ', x,x, 7 * ' ')
            print(5 *' ', x, 13*' ', x, 5* ' ')
            print(3* ' ', x, 17 *' ', x, 3* ' ')
            print(3* ' ', x, ' ', y,y,y, ' ', y,y,y, ' ', x, 3* ' ')
            print( ' ', x, 3* ' ', y, ' ', y, ' ', y, ' ', y, 3 * ' ', x, ' ')
            print( ' ', x, 21 * ' ', x, ' ')
            print( ' ', x, 3 * ' ', y, 9 * ' ', y, 3 * ' ', x, ' ')
            print(3* ' ', x, ' ', y,y, 5 *' ',y,y, ' ', x, 3* ' ')
            print(3* ' ', x, 3*' ', y,y,y,y,y, 3 *' ', x, 3* ' ')
            print(5 *' ', x, 13*' ', x, 5* ' ')
            print(7 * ' ', x,x, 5 * ' ', x,x, 7 * ' ')
            print(11 * ' ', x,x,x, 11 * ' ')
            print(3*' ', "Wygrana! W ", sum, 'ruchach')

            break
        

macierz = [[1, 1, 1, 1, 1, 1, 1], 
[1, 2, 1, 0, 0, 0, 1],
[1, 0, 1, 0, 1, 1, 1],
[1, 0, 0, 0, 0, 0, 1],
[1, 0, 1, 1, 1, 0, 1],
[1, 0, 0, 0, 1, 3, 1],
[1, 1, 1, 1, 1, 1, 1]]

n = 20

gracz = [1,1]
meta = [5,5]
puste=' '
sciana = '#'
ludzik = 'O'
drzwi = 'X'
gra(macierz, n, gracz, meta)