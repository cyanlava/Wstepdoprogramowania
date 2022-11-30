import math 

def find_hypothenuse(cathetus1, cathetus2):
    '''
    Function takes two catheti and calculates the hypothenuse of
    the triangle
    '''
    hypothenuse = math.sqrt(cathetus1**2 + cathetus2**2)
    return hypothenuse

def main():
    '''
    Main function that calculates per the find_hypothenuse function for 
    values 3 and 4
    '''
    a = 3
    b = 4
    c = find_hypothenuse(a, b)

if __name__ == '__main__':
    '''
    The above statement runs the main function if the script is run independently,
    and not as a module. Good for testing?
    '''
    main()

