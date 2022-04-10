# 11724
import sys
input = sys.stdin.readline
N, M = map(int, input().strip().split())
edges = {i: [] for i in range(1, N+1)}
for _ in range(M) :
    s, e = map(int, input().strip().split())
    edges[s] = edges[s] + [e]
    edges[e] = edges[e] + [s]
visited = [False] * (N+1)

count = 0
def DFS(s) :
    global count
    count += 1
    queue = [s]
    while queue :
        c = queue.pop()
        if visited[c] : continue
        else : visited[c] = True
        [queue.append(e) for e in edges[c] if not visited[e]]


[DFS(i) for i in range(1, N+1) if not visited[i]]
print(count)