towar = [{'nazwa': 'banan', 'jednostka': 'kg', 'ilosc': 10, 'cena': 3},
{'nazwa': 'jabłko', 'jednostka': 'kg', 'ilosc': 16, 'cena': 2.5},
{'nazwa': 'mąka pszenna', 'jednostka': 'op.', 'ilosc': 30, 'cena': 2.5},
{'nazwa': 'mydło', 'jednostka': 'szt.', 'ilosc': 6, 'cena': 1.5},
{'nazwa': 'jogurt naturalny', 'jednostka': 'szt.', 'ilosc': 20, 'cena': 1.5},
{'nazwa': 'papier toaletowy 8 rolek', 'jednostka': 'op.', 'ilosc': 10, 'cena': 9}]

def wyszukaj(towar, nazwa):
    toggle = 0
    for i in towar:
        for key, value in i.items():
            if key == 'nazwa':
                if value == nazwa:
                    toggle = 1
                    wynik = i

    if toggle == 1:
        return wynik
    else:
        return('nie ma wśród towarów')
                

def sumuj(towar, nazwa):
    for i in towar:
        for key, value in i.items():
            if key == 'nazwa':
                if value == nazwa:
                    sum = i['ilosc'] * i['cena']
                    return sum

def sumuj_wszystko(towar):
    sum = 0
    for i in towar:
        sum = sum + i['ilosc'] * i['cena']
    return sum

def dodaj_towar(towar, nazwa,jednostka, ilosc, cena):
    entry = {'nazwa': str(nazwa), 'jednostka': str(jednostka), 'ilosc': int(ilosc), 'cena': int(cena)}
    towar.append(entry)

def aktualizuj_ilosc(towar, nazwa, ilosc):
    toggle = 0
    for i in towar:
        for key, value in i.items():
            if key == 'nazwa':
                if value == nazwa:
                    toggle = 1
                    i['ilosc'] = ilosc

    if toggle == 1:
        return towar

    if toggle == 0:
        return 'nie ma towaru o takiej nazwie'

def filtr_jednostka(towar, jednostka):
    list = []
    toggle = 0
    for i in towar:
        if i['jednostka'] == jednostka:
            list.append(i)
            toggle = 1
    if toggle == 1:
        return list
    else:
        return 'nie ma towaru w takiej jednostce'

                

def main():
    a = filtr_jednostka(towar, 'g')

    
    print(a)

if __name__ == '__main__':
    main()
