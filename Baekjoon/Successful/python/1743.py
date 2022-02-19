# 1743
import sys
input = sys.stdin.readline

n, m, k = map(int, input().strip().split())
coo = [[False] * m for _ in range(n)]
v = [[False] * m for _ in range(n)]
for _ in range(k) :
    x, y = map(int, input().strip().split())
    coo[x-1][y-1] = True

def bfs(x, y) :
    q = [(x,y)]
    av = [(-1, 0), (1, 0), (0, 1), (0, -1)]
    count = 0
    while q :
        x1, y1 = q.pop(0)
        if v[x1][y1] : continue
        v[x1][y1] = True
        count += 1
        for a, b in av :
            if 0 <= x1+a < n and 0 <= y1+b < m and coo[x1+a][y1+b] and not v[x1+a][y1+b] :
                q.append((x1+a, y1+b))
    return count

result = 0
for x in range(n) :
    for y in range(m) :
        if coo[x][y] and not v[x][y] : result = max(bfs(x, y), result)
print(result)

