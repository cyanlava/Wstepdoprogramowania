def binary(n):
    if n == 0:
        return n
    else:
        return n%2 + 10 * (binary(n/2))

def main():
    print(binary(156))

if __name__ == '__main__':
    main()
