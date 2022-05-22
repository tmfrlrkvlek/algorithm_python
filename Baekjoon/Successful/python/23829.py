# 23829
import sys
input = sys.stdin.readline
N, Q = map(int, input().split())
Ps = sorted(map(int, input().split()))
dp = []
sum_value = 0
for p in Ps :
    sum_value += p
    dp.append(sum_value)

for _ in range(Q) :
    X = int(input().strip())
    l = 0; r = N-1
    result = N
    while l <= r :
        mid = (l+r)//2
        if Ps[mid] < X :
            l = mid+1
        else :
            result = mid
            r = mid-1
    print(((X*result - dp[result-1]) if result > 0 else 0) + (dp[N-1] - (dp[result-1] if result > 0 else 0) - X*(N-result)))
