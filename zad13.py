x = 7568723
m = []
for i in range(2, x):
    if x % i == 0:
        m.append(i)



if len(m) == 0:
    print("liczba pierwsza")
else:
    print("nie jest to liczba pierwsza")
