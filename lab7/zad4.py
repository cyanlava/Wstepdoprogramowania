def find_max(dict):
    max = dict[1]
    for i in dict:
       if max < dict[i]:
        max = dict[i]
    
    return max
        
    

def main():
    a = find_max({1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2})
    print(a)
if __name__ == '__main__':
    main()
    
    