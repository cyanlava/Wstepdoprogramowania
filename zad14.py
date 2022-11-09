y = input
x = int(y)
print(x%10)
print((x - x%10)/10 % 10)
#to samo co wyzej, tylko liczba calkowita
print((int)((x - x%10)/10 % 10))


sum=0
pum=0

for digit in str(x):
    sum=sum + 1
    pum=pum + int(digit)

print(x)
print(sum)
print("suma cyfr wynosi ", pum)
