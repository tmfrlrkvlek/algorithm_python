maxv = 0
idx = 0
for i in range(9):
    a = int(input())
    if maxv < a :
        maxv = a
        idx = i + 1
print("%d\n%d" %(maxv,idx))
