import math 

def find_hypothenuse(cathetus1, cathetus2):
    hypothenuse = math.sqrt(cathetus1**2 + cathetus2**2)
    return hypothenuse

def main():
    a = 3
    b = 4
    c = find_hypothenuse(a, b)

if __name__ == '__main__':
    main()

