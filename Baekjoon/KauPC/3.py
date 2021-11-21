import sys
input = sys.stdin.readline

n, m = map(int, input().split())
rooms = [list(map(int, input().split())) for _ in range(n)]
graph = [[[] for _ in range(m)] for _ in range(n)]
d = [[-1 for _ in range(m*n)] for _ in range(m*n)]

for i in range(n):
    for j in range(m):
        if rooms[i][j] == 0 : continue
        if j < m-1 and rooms[i][j+1]: 
            graph[i][j].append([i,j+1])
            graph[i][j+1].append([i,j])
        if i < n-1 and rooms[i+1][j]:
            graph[i][j].append([i+1,j])
            graph[i+1][j].append([i,j])

def bfs(s, graph) -> int:
    c = [[-1 for _ in range(m)] for _ in range(n)]
    q = [s]
    c[s[0]][s[1]] = 0
    d[s[0]*m+s[1]][s[0]*m+s[1]] = 0
    while q :
        cp = q.pop(0)
        depth = c[cp[0]][cp[1]] + 1
        for p in graph[cp[0]][cp[1]]:
            if c[p[0]][p[1]] == -1 :
                c[p[0]][p[1]] = depth
                d[s[0]*m+s[1]][p[0]*m+p[1]] = depth
                q.append(p)

for i in range(n):
    for j in range(m):
        if rooms[i][j] : 
            bfs([i,j], graph)
maxD = -1
pw = 0
for i in range(m*n):
    for j in range(m*n):
        if d[i][j] >= maxD :
            x1, y1 = i//m, i%m
            x2, y2 = j//m, j%m
            pw2 = rooms[x1][y1] + rooms[x2][y2]
            pw = pw2 if d[i][j] > maxD else pw2 if pw2 > pw else pw
            maxD = d[i][j]
print(pw)