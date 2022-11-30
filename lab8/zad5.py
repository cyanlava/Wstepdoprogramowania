def sum_rec(n):
    if n==1:
        return 1
    elif n<1:
        return 'nie jest to liczba naturalna'
    else:
        return n+sum_rec(n-1)
def main():
    print(sum_rec(5))

if __name__ == '__main__':
    main()

'''
Pytania i odpowiedzi:)) czyli zadanie 5:

a) niejako tak - najpierw zostanie uruchomiony sum_rec(2), 
wezwany przez sum_rec(3). Następnie sum_rec(2) uruchomi sum_rec(1)

b) nie

c) 10

'''