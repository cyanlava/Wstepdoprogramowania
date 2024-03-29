def najednejlinii(p1, p2, p3):
    p = (p2[0] - p1[0]) * (p3[1] - p1[0]) - (p2[1] - p1[1]) * (p3[0] - p1[0])
    if p == 0:
        return True
    else:
        return False

def obwod(p1, p2, p3):
    if najednejlinii(p1, p2, p3):
        print("Podane punkty nie tworzą trójkąta - 0")
    else:
        x1 = p1[0] - p2[0]
        y1 = p1[1] - p2[1]
        o1 = (x1*x1 + y1*y1)
        l1 = o1**0.5

        x2 = p1[0] - p3[0]
        y2 = p1[1] - p3[1]
        o2 = (x2*x2 + y2*y2)
        l2 = o2**0.5

        x3 = p3[0] - p2[0]
        y3 = p3[1] - p2[1]
        o3 = (x3*x3 + y3*y3)
        l3 = o3**0.5

        o = l1+l2+l3
        return o
    

print(obwod([0, 0], [3, 3], [4, 4]))