# 2343
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())
ls = list(map(int, input().strip().split()))
l = 0; r = sum(ls)
result = r+1
def count(mid) :
    count = 0
    remain = 0
    maxSize = 0
    for l in ls :
        remain += l
        if remain > mid :
            maxSize = max(remain-l, maxSize)
            remain = l
            count += 1
    if remain : 
        maxSize = max(remain, maxSize)
        count += 1
    return count, maxSize
while l <= r :
    mid = (l+r)//2
    cnt, size = count(mid)
    if cnt <= m :
        result = min(result, size)
        r = mid-1
    else : l = mid+1
print(result)



