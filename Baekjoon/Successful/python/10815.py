# 10815
import sys
input = sys.stdin.readline
n = int(input().strip())
ns = sorted(list(map(int, input().strip().split())))
_ = input().strip()
ms = list(map(int, input().strip().split()))
def find(m) :
    l = 0; r = n-1
    while l <= r :
        mid = (l+r)//2
        if ns[mid] == m : return True
        elif ns[mid] < m : l = mid+1
        else : r = mid-1
    return False
for m in ms : print(1 if find(m) else 0, end = " ")