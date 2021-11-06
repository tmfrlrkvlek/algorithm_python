# 23292
import sys
input = sys.stdin.readline
b = input()
maxV = 0; day = ""
for _ in range(int(input())) :
    d = input()
    m = [(int(b[i])-int(d[i]))**2 for i in range(8)]
    v = sum(m[0:4])*sum(m[4:6])*sum(m[6:8])
    if maxV < v : (maxV, day) = (v, d)
    elif maxV == v : day = d if d < day else day
print(day)