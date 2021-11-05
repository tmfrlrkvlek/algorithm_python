# 21735
import sys
input = sys.stdin.readline
n, m = map(int, input().split())
a = list(map(int, input().split()))

def dfs(s, current, time) :
    if s > 0 : current += a[s-1]
    if time == m or s >= n: return current
    s1 = dfs(s+1, current, time+1) if s+1 <= n else 0
    s2 = dfs(s+2, current//2, time+1) if s+2 <= n else 0
    return max(s1, s2)

print(dfs(0, 1, 0))