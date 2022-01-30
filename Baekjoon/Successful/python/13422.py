# 13422
import sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t) :
    n, m, k = map(int, input().strip().split())
    ma = list(map(int, input().strip().split()))
    if n == m : print(1 if sum(ma) < k else 0)
    else :
        ma += ma[:m-1]
        s = sum(ma[:m-1])
        result = 0
        for l in range(n) :
            s += ma[l+m-1]
            if s < k : result += 1
            s -= ma[l]
        print(result)

