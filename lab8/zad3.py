def silnia(n):
    #Polacy nie gesi smh
    l = 1
    for i in range(1, n+1):
        l = l*i 
    return l
    


def main():
    print(silnia(4))

if __name__ == '__main__':
    main()