# 1753
import heapq
input = __import__('sys').stdin.readline
V, E = map(int, input().strip().split())
K = int(input().strip())
graph = {i: [] for i in range(1, V+1)}
for _ in range(E) :
    u, v, w = map(int, input().strip().split())
    graph[u] += [(w, v)]
dists = [float('inf') for _ in range(V+1)]
dists[K] = 0
queue = [(0, K)]
while queue :
    dist, v = heapq.heappop(queue)
    if dists[v] < dist : continue
    else :
        for (w, v) in graph[v] :
            if dists[v] > dist + w :
                dists[v] = dist + w
                heapq.heappush(queue, (dist+w, v)) 
[print(i if i < float('inf') else 'INF') for i in dists[1:]]
