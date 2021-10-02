import math
import copy

n, m, l = map(int, input().split())
if n > 0 : loc = list(map(int, input().split()))
else : loc = []
loc.append(l)
loc.sort()
d = []
d.append(loc[0])
for i in range(1, len(loc)) :
    d.append(loc[i] - loc[i - 1])

c = [0] * len(d)
cd = copy.deepcopy(d)
while m > 0 :
    cds = sorted(cd, reverse=True)
    index = cd.index(cds[0])
    c[index] += 1
    cd[index] = math.ceil(d[index] / (c[index] + 1))
    m -= 1
print(max(cd))
