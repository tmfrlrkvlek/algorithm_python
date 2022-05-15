# 풀이중

import heapq

def solution(n, start, end, roads, traps):
    MAX = float('inf')
    def dijkstra(s, e) :
        queue = [(0, s, [0]*(n+1))]
        dists = [MAX] * (n+1)
        dists[s] = 0
        while queue :
            dist, current, trap = heapq.heappop(queue)
            if dists[current] < dist :
                continue
            if dist != 0 and current in traps:
                trap[current] = 1 if trap[current] == 0 else 0
            print(current, graph[current])
            for nxt, cost in graph[current] :
                print(int(trap[current]) + int(trap[nxt]))
                if (int(trap[current]) + int(trap[nxt])) % 2 :
                    continue
                print(dists[nxt])
                if dists[nxt] > dist+cost :
                    dists[nxt] = dist+cost
                    heapq.heappush(queue, (dist+cost, nxt, trap))
            print(current, graph_reverse[current])
            for nxt, cost in graph_reverse[current] :
                if not (int(trap[current]) + int(trap[nxt])) % 2 :
                    continue
                if dists[nxt] > dist+cost :
                    dists[nxt] = dist+cost
                    heapq.heappush(queue, (dist+cost, nxt, trap))
            print(queue)
        print(dists)
        return dists[e]
            
    MAX = float('inf')
    graph = {i : [] for i in range(1, n+1)}
    graph_reverse = {i : [] for i in range(1, n+1)}
    for road in roads :
        p, q, s = (road[0], road[1], road[2])
        graph[p].append((q, s))
        graph_reverse[q].append((p, s))
    return dijkstra(start, end)

# print(solution(3, 1, 3, [[1,2,2], [3, 2,3]], [2]))
print(solution(4, 1, 4, [[1, 2, 1], [3, 2, 1], [2, 4, 1]], [2, 3]))