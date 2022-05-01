import heapq

inf = float('inf')

def solution(n, s, a, b, fares):
    graph = {i: [] for i in range(1, n+1)}
    for fare in fares :
        n1, n2, f = (fare[0], fare[1], fare[2])
        graph[n1].append((n2, f)); graph[n2].append((n1, f))
    starts, starta, startb = (dijkstra(graph, n, s), dijkstra(graph, n, a), dijkstra(graph, n, b))
    answer = inf
    for mid in range(1, n+1) :
        answer = min(answer, starts[mid]+starta[mid]+startb[mid])
    return answer

def dijkstra(graph, n, s) :
    fare = [inf for _ in range(n+1)]
    fare[s] = 0
    queue = [(0, s)]
    while queue :
        fee, c = heapq.heappop(queue)
        if fare[c] < fee : continue
        for (d, cost) in graph[c] :
            if fare[d] <= fee+cost : continue
            fare[d] = fee+cost
            heapq.heappush(queue, (fee+cost, d))
    return fare