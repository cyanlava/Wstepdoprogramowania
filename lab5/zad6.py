o = 9
n = 2

l = []

while o >= n:
    for i in range(2, n):
        if n%i == 0:
            l.append(i)
    n += 1

print(l)

