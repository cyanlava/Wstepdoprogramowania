x = int(input("podaj liczbe"))





sum=0
pum=0

for digit in str(x):
    sum=sum + 1
    pum=pum + int(digit)

print(x)
print(sum)
print("suma cyfr wynosi ", pum)
