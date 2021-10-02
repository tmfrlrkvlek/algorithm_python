# 1912

n = int(input())
num = list(map(int, input().split(' ')))
n -= 1
biggest = num[n]
total = num[n]
while(n > 0):
    n -= 1
    new = num[n]
    if(new < 0 and biggest < total) :
        biggest = total
    total += new
    if(total < new):
        total = new
if(biggest < total):
    biggest = total
print(biggest)