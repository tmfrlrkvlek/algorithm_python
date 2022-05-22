# 14948
import sys
from heapq import *
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
cost_unused = [[float('inf') for _ in range(m)] for _ in range(n)]
cost_used = [[float('inf') for _ in range(m)] for _ in range(n)]
cost_unused[0][0] = graph[0][0]
cost_used[0][0] = graph[0][0]
def dijkstra() :
    hq = [(cost_unused[0][0], False, 0, 0)]
    while hq :
        cost, used, x, y = heappop(hq)
        if (not used) and cost_unused[x][y] < cost :
            continue
        elif used and cost_used[x][y] < cost :
            continue
        for a, b in [(1, 0), (-1, 0), (0, 1), (0, -1)] :
            nx, ny = x+a, y+b
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            ncost = max(cost, graph[nx][ny])
            if (not used) and cost_unused[nx][ny] > ncost:
                cost_unused[nx][ny] = ncost
            elif used and cost_used[nx][ny] > ncost:
                cost_used[nx][ny] = ncost
            else :
                continue
            heappush(hq, (ncost, used, nx, ny))
        if used :
            continue
        for a, b in [(2, 0), (-2, 0), (0, 2), (0, -2)] :
            nx, ny = x+a, y+b
            if not (0 <= nx < n and 0 <= ny < m) :
                continue
            ncost = max(cost, graph[nx][ny])
            if cost_used[nx][ny] > ncost:
                cost_used[nx][ny] = ncost
                heappush(hq, (ncost, True, nx, ny))
    return min(cost_unused[n-1][m-1], cost_used[n-1][m-1])
print(dijkstra())