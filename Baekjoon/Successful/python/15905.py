# 15905
import sys, heapq
input = sys.stdin.readline
N = int(input().strip())
infos = []
for _ in range(N) :
    c, p = map(int, input().strip().split())
    heapq.heappush(infos, (8-c, 100000-p))
[heapq.heappop(infos) for _ in range(4)]
c = heapq.heappop(infos)[0]
result = 0
while infos :
    n = heapq.heappop(infos)[0]
    if n == c : result += 1
    else : break
print(result)
