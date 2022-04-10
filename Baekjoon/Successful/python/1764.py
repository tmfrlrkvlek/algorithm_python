# 1764
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
listen = sorted([input().strip() for _ in range(N)])
see = sorted([input().strip() for _ in range(M)])

l = 0; s = 0
result = []

while l < N and s < M :
    if listen[l] < see[s] : l += 1
    elif listen[l] > see[s] : s += 1
    else : 
        result.append(listen[l])
        l += 1; s += 1
print(len(result))
print('\n'.join(result))