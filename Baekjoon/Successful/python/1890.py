# 1890
import sys
input = sys.stdin.readline
N = int(input().strip())
graph = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]
dp[N-1][N-1] = 1
def find(x, y) :
    if x == y == N-1 : return
    dp[x][y] = (dp[x][y+graph[x][y]] if 0 <= y+graph[x][y] < N else 0) + (dp[x+graph[x][y]][y] if 0 <= x+graph[x][y] < N else 0)
[[find(j, i) for j in range(N-1, -1, -1)] for i in range(N-1, -1, -1)]
print(dp[0][0])