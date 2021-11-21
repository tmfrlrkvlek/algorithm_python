# 1051
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
rect = [list(str(input().rstrip())) for _ in range(n)]
mx = 0
for i in range(n - 1):
    for j in range(m - 1):
        for k in range(j + 1, m):
            gap = k - j
            if k >= m or i+gap >= n : break
            if rect[i][j] == rect[i][k] == rect[i+gap][k] == rect[i+gap][j] :
                mx = max(gap, mx)
print((mx+1)**2)