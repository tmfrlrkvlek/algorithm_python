# 14627
import sys
input = sys.stdin.readline
s, c = map(int, input().strip().split())
ls = [int(input()) for _ in range(s)]
l = 0; r = max(ls)
result = 1
while l <= r :
    mid = (l+r)//2
    if mid == 0 : 
        if s < c : result = 0
        break
    count = 0
    for lg in ls : count += (lg//mid)
    if count >= c : 
        result = mid
        l = mid+1
    else : r = mid-1
print(sum(ls)-c*result)
