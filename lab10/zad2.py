import time
i = 0
tmp=2
while i < 30:
    print(i)
    i = i + 1
    time.sleep(tmp)
    tmp=0.8 * tmp