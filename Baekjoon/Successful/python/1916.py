# 1916
import sys, heapq
input = sys.stdin.readline
N = int(input().strip())
M = int(input().strip())
edges = {i:[] for i in range(1, N+1)}
for _ in range(M) :
    s, e, w = map(int, input().strip().split())
    edges[s] += [(e, w)]
start, end = map(int, input().strip().split())
queue = [(0, start)]
dists = [float('inf')] * (N+1)
dists[start] = 0
while queue :
    dist, current = heapq.heappop(queue)
    if dists[current] < dist : continue
    else :
        for (v, w) in edges[current] :
            if dist + w < dists[v] :
                dists[v] = dist + w
                heapq.heappush(queue, (dist+w, v))
print(dists[end])

