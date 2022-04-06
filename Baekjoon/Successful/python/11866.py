# 11866
import sys
input = sys.stdin.readline

N, K = map(int, input().strip().split())
ps = [i for i in range(1, N+1)]
i = K-1
result = []
for _ in range(N-1) :
    result.append(ps[i])
    del ps[i]
    i += K-1
    if i >= len(ps) : i %= len(ps)
print('<', end='')
[print(i, end=', ') for i in result]
print(ps[0], end='>')