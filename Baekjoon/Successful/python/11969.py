# 11969
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
dp = [(0, 0, 0)]
a, b, c = 0, 0, 0
for i in range(N) :
    num = int(input().strip())
    if num == 1 :
        a += 1
    elif num == 2 :
        b += 1
    else :
        c += 1
    dp.append((a, b, c))

for _ in range(Q) :
    a, b = map(int, input().split())
    print(' '.join(map(str,[dp[b][0] - dp[a-1][0], dp[b][1] - dp[a-1][1], dp[b][2] - dp[a-1][2]])))