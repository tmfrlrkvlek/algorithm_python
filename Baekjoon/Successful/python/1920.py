# 1920
import sys
input = sys.stdin.readline
n = int(input().strip())
ns = sorted(list(map(int, input().strip().split())))
_ = input().strip()
ms = list(map(int, input().strip().split()))
for m in ms :
    l = 0; r = n-1
    isExist = False
    while l <= r :
        mid = (l+r)//2
        if ns[mid] == m : 
            isExist = True
            break
        elif ns[mid] < m : l = mid+1
        else : r = mid-1
    print(1 if isExist else 0)



