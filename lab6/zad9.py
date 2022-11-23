
def odleglosc(p1, p2):
    x = p1[0] - p2[0]
    y = p1[1] - p2[1]
    o = (x*x + y*y)
    l = o**0.5
    return l
    


print(odleglosc([0, 4], [4, 0]))