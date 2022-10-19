m = [6, 5, 46, 3, 754, 243]
n = [-3, -2, -9, -1]

j = n[:1]
print(j)

min = 0
max = 0
for i in m:
    if i > max:
        max = i

print(max)