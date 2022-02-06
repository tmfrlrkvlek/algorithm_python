# 1654
import sys
input = sys.stdin.readline

k, n = map(int, input().strip().split())
ls = [int(input().strip()) for _ in range(k)]

l = 1; r = max(ls)
result = 0

def count(mid) :
    count = 0
    for l in ls : count += (l//mid)
    return count

while l <= r :
    mid = (l+r)//2
    if count(mid) >= n :
        result = max(mid, result)
        l = mid+1
    else : r = mid-1
print(result)
