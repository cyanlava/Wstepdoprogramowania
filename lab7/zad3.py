import math 

def find_hypothenuse(cathetus1, cathetus2):
    '''
    Function takes two catheti and calculates the hypothenuse of
    the triangle
    '''
    hypothenuse = math.sqrt(cathetus1**2 + cathetus2**2)
    return hypothenuse

def find_angles(cathetus1, cathetus2):
    '''
    The function first calculates the missing hypothenuse and then calculates
    the angles using the law of cosines.
    '''
    a = cathetus1
    b = cathetus2
    c = math.sqrt(a**2 + b**2) 
    '''
    I ditched the find.hypothenuse function
    for calculating the hypotenuse so that the function could be run
    independently
    '''
    l1 = math.degrees(math.acos((a * a + c * c - b * b)/(2 * a * c)))
    l2 = math.degrees(math.acos((b * b + c * c - a * a)/(2 * b * c)))
    return l1, l2

def main():
    '''
    Main function that calculates per the find_hypothenuse function for 
    values 3 and 4
    '''
    a = 3
    b = 4
    c = find_hypothenuse(a, b)
    print(find_angles(3, 4))

if __name__ == '__main__':
    '''
    The above statement runs the main function if the script is run independently,
    and not as a module.
    '''
    main()
