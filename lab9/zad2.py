a = input('podaj 10 liczb (oddziel je spacjami) ')
m = a.split(" ")
list=[]
for i in m:
    i = int(i)
    list.append(i)
if len(m) != 10:
    print('za duza badz za krotka lista')
else:
    list.reverse()
    s = 0
    for i in list:
        if i>s:
            s = i
    list.remove(s)
    list.append(s)
    print(list)
    print(list[0])
 