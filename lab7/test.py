a = {1: 10, 2: 7, 3: 8, 4: 15, 5: 14, 6: 3, 7: 2}
b = {8: 10, 9: 40, 10: 34, 11: 100}

for key, value in b.items():
    a[key] = value

print(a)
    
