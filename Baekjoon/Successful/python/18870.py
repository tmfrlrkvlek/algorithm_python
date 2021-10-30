n = int(input())
l = list(map(int, input().split()))
s = sorted(set(l))
d = {}
for i, x in enumerate(s): d[x] = i
for k in l: print(d[k], end=" ")