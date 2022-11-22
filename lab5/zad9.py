x = 42367
sum = 0
while x > 0:
    r = x%10
    sum=sum+r
    x=(x/10)-(r/10)

print(int(sum))