# 2805
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
ls = list(map(int, input().strip().split()))

def length(mid) :
    count = 0
    for l in ls : 
        if l > mid : count += l-mid
    return count

l = 0; r = 1000000000
result = 0
while l <= r :
    mid = (l+r)//2
    if length(mid) >= m :
        result = mid
        l = mid+1
    else : r = mid-1
print(result)
