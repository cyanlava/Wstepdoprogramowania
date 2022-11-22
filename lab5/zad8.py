from random import randint

x = randint(0, 100)

p = 0
while True:
    s = int(input("wpisz liczbe!"))
    p+=1
    print("liczba prób: ", p)
    if s == x:
        print('wygrana!')
        break
    else:
        print('sprobuj ponownie!')
        if s > x:
            print("za duża!")
        else: 
            print("za mała!")