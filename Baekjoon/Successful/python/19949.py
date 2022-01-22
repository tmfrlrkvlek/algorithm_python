# 19949
import sys
answer = list(map(int, sys.stdin.readline().rstrip().split()))
count = 0

def dp(idx, c, ba, an) :
    global count
    if an == answer[idx] : c += 1
    if idx == 9 : 
        if c >= 5 : count += 1
        return
    else : [dp(idx+1, c, an, k) for k in range(1, 6) if not (ba == an == k)]
[dp(0, 0, -1, i) for i in range(1, 6)]
print(count)