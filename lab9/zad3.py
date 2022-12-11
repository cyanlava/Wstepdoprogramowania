def rectangle_area(a, b):
    if a<=0 and b<=0:
        return 'a i b musza byc dodatnie'
    else:
        return a*b


def main():
    print(rectangle_area(3,4))

if __name__ == '__main__':
    main()