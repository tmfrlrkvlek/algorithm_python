# 15810
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
A = list(map(int, input().strip().split()))
l = 0; r = A[0]*m

def avail(mid) :
    sumV = 0
    for a in A : sumV += mid//a
    return sumV >= m

result = r
while l <= r :
    mid = (l+r)//2
    if avail(mid) : 
        r = mid-1
        result = mid
    else : l = mid+1
print(result)

