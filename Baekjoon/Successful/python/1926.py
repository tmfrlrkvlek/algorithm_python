# 1926
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().strip().split())
p = []
v = [[False] * m for _ in range(n)]
if m == 1 : p = [[int(input().strip())] for _ in range(n)]
else : p = [list(map(int, input().strip().split())) for _ in range(n)]

def bfs(x, y) :
    q = deque([(x, y)])
    area = 0
    while q :
        x1, y1 = q.popleft()
        if v[x1][y1] : continue
        v[x1][y1] = True
        area += 1
        for a, b in [(-1, 0), (1, 0), (0, -1), (0, 1)] :
            if 0 <= x1+a < n and 0 <= y1+b < m and p[x1+a][y1+b] and not v[x1+a][y1+b] : 
                q.append((x1+a, y1+b))
    return area

count = 0
maxArea = 0
for x in range(n) :
    for y in range(m) :
        if (not v[x][y]) and p[x][y] :
            count += 1
            maxArea = max(bfs(x, y), maxArea)
print(count)
print(maxArea)
