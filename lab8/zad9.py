def factorize(n):
    m = 2
    lista =[]
    if n<=m:
        lista.append(n)
    else:
        while n%m != 0:
            m+=1
        if n==m:
            lista.append(n)
        else:
            lista.append(m)
            lista = lista + factorize(n//m)
        print(lista)

    



def main():
    factorize(50)

if __name__ == '__main__':
    main()




while i<=n and n%i!=0:
    i+=1
    if (n%i==0)
        retun 
