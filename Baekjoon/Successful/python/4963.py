# 4963
import sys
input = sys.stdin.readline

while True :
    w, h = map(int, input().strip().split())
    if w ==0 and h == 0 : break
    m = []
    if w <= 1 :
        m = [[int(input())] for _ in range(h)]
    else :
        m = [list(map(int, input().strip().split())) for _ in range(h)]
    v = [[False] * w for _ in range(h)]
    avail = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (1, -1), (1, 0), (1, 1)]

    def bfs(x, y) :
        q = [(x, y)]
        while q :
            x1, y1 = q.pop(0)
            if v[x1][y1] : continue
            v[x1][y1] = True
            [q.append((x1+a, y1+b)) for a, b in avail if 0 <= x1+a < h and 0 <= y1+b < w and (not v[x1+a][y1+b]) and m[x1+a][y1+b] == 1]
    count = 0
    for x in range(h) :
        for y in range(w) :
            if (not v[x][y]) and m[x][y] == 1 : 
                bfs(x, y)
                count += 1
    print(count)