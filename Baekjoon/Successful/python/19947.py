# 19947
import sys
from math import floor as f
h, y = map(int, sys.stdin.readline().rstrip().split())
dp = [h for _ in range(y+1)]
for c in range(0, y) :
    if y-c >= 5 :
        dp[c+5] = max(f(dp[c]*1.35), dp[c+5]) 
    if y-c >= 3 :
        dp[c+3] = max(f(dp[c]*1.2), dp[c+3]) 
    if y-c >= 1 :
        dp[c+1] = max(f(dp[c]*1.05), dp[c+1]) 
print(max(dp))

