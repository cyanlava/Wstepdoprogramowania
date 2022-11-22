liczba = int(input('Podaj liczbe dodatnią: '))

i = 1 
suma = 0

while suma <= liczba: 
    if suma + i > liczba:
        break
    else:
        i += 1
        suma = suma + i
        
    print (suma, i)

wynik = "Liczba pierwszych dodatnich liczb naturalnych, których suma jest niewiększa niż {} wynosi {}"
wynik = wynik.format (liczba, i)
print(wynik)