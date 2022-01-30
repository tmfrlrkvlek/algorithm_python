# 15686
import sys
from itertools import combinations as cb
input = sys.stdin.readline
n, m = map(int, input().strip().split())
ci = []
house = []
chicken = []
for x in range(n) :
    ci.append(list(map(int, input().strip().split())))
    for idx, c in enumerate(ci[-1]) :
        if c == 0 : continue
        elif c == 1 : house.append((x, idx))
        else : chicken.append((x, idx))
hi = [[0] * len(chicken) for _ in range(len(house))]
for i, h in enumerate(house) :
    for j, c in enumerate(chicken) :
        hi[i][j] = abs(h[0]-c[0])+abs(h[1]-c[1])
minD = n*2*len(house)
for s in cb(range(len(chicken)), len(chicken)-m) :
    d = 0
    for i, h in enumerate(house) :
        d += min([c for j, c in enumerate(hi[i]) if j not in s])
    minD = min(minD, d)
print(minD)
