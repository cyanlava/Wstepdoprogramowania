def factorial(n): 
    if n == 1:
        return 1
    else:
        return factorial(n-1)*n
def main():
    print(factorial(3))
if __name__ == '__main__':
    main()