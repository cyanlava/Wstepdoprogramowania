def permute(a, l, r):
    if l == r:
        print('print a', a, 'l, r', l, r)
    else:
        for i in range(l, r+1):
            a[l], a[i] = a[i], a[l]
            print("l", l, 'i', i)
            print(a)
            permute(a, l+1, r)
            a[l], a[i] = a[i], a[l]
            print("l", l, 'i', i)
            print(a, 'aaaaaaa')
a = ['A', 'B', 'C']
permute(a, 0, len(a)-1)

#r jest stale for i in range matrycy 
'''

'''