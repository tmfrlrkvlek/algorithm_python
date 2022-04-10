# 1932
import sys
input = sys.stdin.readline
N = int(input().strip())
triangle = [list(map(int, input().strip().split())) for _ in range(N)]
maxTree = [[float('inf')] * i for i in range(1, N+1)]
maxTree[-1] = triangle[-1]
for i in range(N-2, -1, -1) :
    for j in range(i+1) :
        maxTree[i][j] = triangle[i][j] + max(maxTree[i+1][j], maxTree[i+1][j+1])
print(maxTree[0][0])