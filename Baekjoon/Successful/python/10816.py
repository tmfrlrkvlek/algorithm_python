# 10816
import sys
input = sys.stdin.readline
n = int(input().strip())
ns = sorted(list(map(int, input().strip().split())))
_ = input().strip()
ms = list(map(int, input().strip().split()))
dp = {}

def index(num) :
    l = 0; r = n-1; result = -1
    while l <= r :
        mid = (l+r)//2
        if ns[mid] == num : 
            result = mid
            break
        elif ns[mid] < num : l = mid+1
        else : r = mid-1
    if result < 0 : return 0
    l = r = result
    while ns[l] == num : 
        l -= 1
        if l<0 : break
    while ns[r] == num : 
        r += 1
        if r == n : break
    return r-l-1

for m in ms :
    if m not in dp : dp[m] = index(m)
    print(dp[m], end = " ")
