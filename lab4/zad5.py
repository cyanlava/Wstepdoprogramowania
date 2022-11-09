imiona = input("Podaj imiona oddzielone przecikami:")
m = imiona.split(",")

for i in m:
    if i[-1] == "a" or i[-1] == "A":
        print(i)
