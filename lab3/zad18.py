import math

thelist = []

for a in range(1, 51):
    for b in range(1, 51):
        for c in range(1, 51):
            if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                
                list = [a, b, c]
                list.sort()
                thelist.append(list)

thelist.sort()

for i in thelist:
    if thelist.count(i) > 1:
        print(thelist.count(i))
    for j in thelist:
        if i == j:
            thelist.remove(j)

print(thelist)

print("liczba trojek pitagorejskich to: ", len(thelist))


