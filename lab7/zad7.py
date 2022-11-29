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

def sum_dictionaries(dict1, dict2):
    result = {}
    for key1, value1 in dict1.items():
        for key2, value2 in dict2.items():
            if key1 == key2:
                result[key1] = value1 + value2

    return result

def main():
    a = sum_dictionaries({1: 10, 2: 20, 3: 30, 4: 40},
    {1: 11, 3: 33, 5: 55})
    print(a)
if __name__ == '__main__':
    main()
    