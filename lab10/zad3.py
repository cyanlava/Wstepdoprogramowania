
file = open("liczby.txt", 'x')

for i in range(1, 101):
    L = [str(i), "\n"]
    file.writelines(L)

file.close()

file = open("liczby.txt", 'r')
#print(file.read())

file.close()

file = open("liczby.txt", 'r+')
list=file.readlines()

file.close()

list2=[]
for j in range(len(list)):
    x=list[j].split('\n')
    list2.append(int(x[0]))

#print(list2)
for l in range(len(list2)):
    if list2[l]%2 == 0:
        list2[l] = list2[l] + 10
#print(list2)

file = open("liczby.txt", 'w')

for p in list2:
    L = [str(p), "\n"]
    file.writelines(L)

file = open("liczby.txt", 'r')

print(file.read())

file.close()
