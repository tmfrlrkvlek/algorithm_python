import sys
input = sys.stdin.readline
sys.setrecursionlimit(99999)

n, m, v = map(int, input().split())
g = [[] for _ in range(n)]

for _ in range(m) :
    p1, p2 = map(int, input().split()) 
    g[p1-1].append(p2-1) 
    g[p2-1].append(p1-1) 
[p.sort() for p in g]

def dfs(s) :
    c[s] = True
    print(s+1, end=" ")
    for p in g[s]:
        if not c[p] : dfs(p)
# [dfs(p) for p in g[s] if not c[p]] 
# [True, True, True, False, True]
# [[1, 2], [0, 4], [0, 3], [2, 4], [1, 3]]
# 0번째 노드부터 시작
# 1 2 5 4 3
# 1 [4] [3] [2] 2

def bfs(s) :
    c[s] = True
    print(s+1, end=" ")
    [q.append(p) for p in g[s] if (not c[p]) and (p not in q)]
    while q :
        p = q.pop(0) # 핵심
        if not c[p] : bfs(p)

q = []
c = [False]*n
dfs(v-1)
print()
c = [False]*n
bfs(v-1)