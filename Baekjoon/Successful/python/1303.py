# 1303
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
battle = [list(input().strip()) for _ in range(m)]
v = [[False] * n for _ in range(m)]
av = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def bfs(x, y) :
    q = [(x, y)]
    count = 0
    while q :
        x1, y1 = q.pop(0)
        if v[x1][y1] : continue
        v[x1][y1] = True
        count += 1
        for a, b in av :
            if 0 <= x1+a < m and 0 <= y1+b < n and (not v[x1+a][y1+b]) and battle[x1+a][y1+b] == battle[x][y] :
                q.append((x1+a, y1+b))
    return count ** 2
white = 0
black = 0
for x in range(m) :
    for y in range(n) :
        if not v[x][y] : 
            if battle[x][y] == 'W' : white += bfs(x, y)
            else : black += bfs(x, y)
print(white, black)