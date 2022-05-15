# 72413

import heapq

MAX = float('inf')

def solution(n, s, a, b, fares):
    def dijkstra(n, s, graph) :
        costs = [MAX] * (n+1)
        costs[s] = 0
        queue = [(0, s)]
        while queue :
            cost, current = heapq.heappop(queue)
            if costs[current] < cost : 
                continue
            for fee, next_node in graph[current] :
                if costs[next_node] > cost+fee :
                    costs[next_node] = cost+fee
                    heapq.heappush(queue, (cost+fee, next_node))
        return costs
    
    graph = {i: [] for i in range(1, n+1)}
    
    for fare in fares :
        c, d, f = (fare[0], fare[1], fare[2])
        graph[c].append((f, d))
        graph[d].append((f, c))
        
    s_costs = dijkstra(n, s, graph)
    a_costs = dijkstra(n, a, graph)
    b_costs = dijkstra(n, b, graph)
    
    answer = MAX
    for mid in range(1, n+1) :
        answer = min(answer, s_costs[mid]+a_costs[mid]+b_costs[mid])
    return answer