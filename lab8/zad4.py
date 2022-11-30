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