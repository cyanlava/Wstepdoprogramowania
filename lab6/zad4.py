def powitaj(imie = "b/d"):
    print("czesc "+imie+" !")

def sumuj(a = 0, b = 0):
    print("suma ", a, " i", b, " to", (a+b))

powitaj()
powitaj('jan')
sumuj(3)
sumuj()
sumuj(b=9)
sumuj(a=9)
sumuj(b=4, a=3)