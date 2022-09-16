# 24392
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
bridge = [list(map(int, input().rstrip().split())) for _ in range(N)]
queue = [bridge[0]] + [[0] * M for _ in range(N-1)]
for i in range(1, N) :
    for j in range(M) :
        if bridge[i][j] == 0 :
            continue
        value = queue[i-1][j]
        if 0 < j :
            value += queue[i-1][j-1]
        if j < M-1 :
            value += queue[i-1][j+1]
        queue[i][j] = value % 1000000007
print(sum(queue[-1]) % 1000000007)