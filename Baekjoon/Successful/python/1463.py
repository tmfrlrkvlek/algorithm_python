# 1463
import sys

N = int(sys.stdin.readline().strip())
count = 0
dp = [0] * (N+1)

def count(n, cnt) :
    if dp[n] > 0 : return cnt + dp[n]
    elif n == 1 : return cnt
    else : 
        minCount = count(n-1, cnt+1)
        if n % 2 == 0 : minCount = min(minCount, count(n//2, cnt+1))
        if n % 3 == 0 : minCount = min(minCount, count(n//3, cnt+1))
        dp[n] = minCount - cnt
        return minCount

for i in range(2, N+1) : count(i, 0)
print(dp[N])