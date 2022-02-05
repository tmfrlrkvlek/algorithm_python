# 17130
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
rmap = [list(input().strip()) for _ in range(n)]
dp = [[-1] * m for _ in range(n)]
def find() :
    for x in range(n) :
        for y in range(m) :
            if rmap[x][y] == 'R' : return x, y
k, start = find()
dp[k][start] = 0
result = -1
for y in range(start+1, m) :
    for x in range(n) :
        if rmap[x][y] == '#' : continue
        maxD = dp[x][y-1]
        if x > 0 : maxD = max(maxD, dp[x-1][y-1])
        if x < n-1 : maxD = max(maxD, dp[x+1][y-1])
        dp[x][y] = maxD+1 if rmap[x][y] == 'C' and maxD != -1 else maxD
        if rmap[x][y] == 'O' : result = max(result, dp[x][y])
print(result)
