print("podaj imie i nazwisko:")
im_naz = input()


s = im_naz.split()
l = s[1]
print(s[0] + " " + l.upper())