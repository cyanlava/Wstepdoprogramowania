def fib(n):
    def fibb(n):
        if n<=1: 
            return n
        else:
            return fibb(n-1)+fibb(n-2)
    if n<1:
        return 'nie jest to liczba naturalna'
    else:
        return fibb(n)
    

def main():
    print(fib(6))

if __name__ == '__main__':
    main()
