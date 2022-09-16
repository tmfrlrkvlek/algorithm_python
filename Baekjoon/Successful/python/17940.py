# 17940

import sys, heapq
input = sys.stdin.readline
N, M = map(int, input().strip().split())
info = [int(input().strip()) for _ in range(N)]
maps = {i : [] for i in range(N)}
for i in range(N) :
    line = list(map(int, input().strip().split()))
    for j in range(N) :
        if line[j] == 0 : continue
        maps[i].append((j, line[j]))
        maps[j].append((i, line[j]))
history = [(float('inf'), float('inf')) for _ in range(N)]
# 환승, 요금, 도착지
q = [(0, 0, 0)]
while q :
    trans, cost, cur = heapq.heappop(q)
    if cur == M :
        print(trans, cost)
        break
    elif history[cur][0] > trans or (history[cur][0] == trans and history[cur][1] > cost) :
        history[cur] = (trans, cost)
    else :
        continue
    for dep, fee in maps[cur] :
        t, c = history[dep]
        next_t = trans + (0 if info[dep] == info[cur] else 1)
        next_c = cost + fee
        if t > next_t or (t == next_t and c > next_c) :
            heapq.heappush(q, (next_t, next_c, dep))

