def find_max(dict):
    max = dict[1]
    for i in dict:
        if max < dict[i]:
            max = dict[i]
    
    return max
        
def merge_dict(dict1, dict2):
    dict1.update(dict2)

    return dict1

def merge_dictionaries(dict1, dict2):
    for key, value in dict2.items():
        dict1[key] = value
    return dict1

def odd_sum_dictionary(dict):
    sum = 0
    for i in dict.values():
        if i%2 != 0:
            sum = sum + i

    return sum

def main():
    a = odd_sum_dictionary({1: 55, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2, 8: 10, 9: 40})

    print(a)
if __name__ == '__main__':
    main()
    