# 1806
import sys
input = sys.stdin.readline
n, s = map(int, input().strip().split())
a = list(map(int, input().strip().split()))
l = r = 0
c = a[0]
result = n+1
while (r < n) :
    if c >= s : 
        result = min(result, r-l+1)
        c -= a[l]
        l += 1
    else :
        r += 1
        if r < n : c += a[r]
print(result if result <= n else 0)