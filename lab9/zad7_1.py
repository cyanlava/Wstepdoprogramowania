def permute(a, l, r):
    
    list=[]
    def perm(a, l , r, list):
        if l == r:
            list.append(a)
            
        else:
            for i in range(l, r+1):
                a[l], a[i] = a[i], a[l]
                perm(a, l+1, r, list)
                a[l], a[i] = a[i], a[l]
    perm(a,l,r, list)
    for i in list:
        print(i)
    

a = ['A', 'B', 'C']
permute(a, 0, len(a)-1)
