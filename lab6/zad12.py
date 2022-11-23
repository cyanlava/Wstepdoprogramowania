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

rysujlabirynt([[1, 1, 1, 1, 1, 1, 1], 
    [1, 2, 1, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 3, 1],
    [1, 1, 1, 1, 1, 1, 1]], ' ', '#', 'o', 'x')