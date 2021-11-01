import sys
from collections import deque
input = sys.stdin.readline

n, m, v = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m) :
    p1, p2 = map(int, input().split())
    g[p1-1].append(p2-1)
    g[p2-1].append(p1-1)
[p.sort() for p in g]

def dfs() :
    while q :
        p = q.pop()
        if c[p] : continue
        c[p] = True
        print(p+1, end=" ")
        [q.append(p) for p in g[p][::-1] if not c[p]]
    
def bfs(s) :
    c[s] = True
    print(s+1, end=" ")
    [q.append(p) for p in g[s] if (not c[p]) and (p not in q)]
    while q :
        p = q.popleft()
        c[p] = True
        print(p+1, end=" ")
        [q.append(p2) for p2 in g[p] if (not c[p2]) and (p2 not in q)]

q = [v-1]
c = [False]*n
dfs()
print()
q = deque()
c = [False]*n
bfs(v-1)

