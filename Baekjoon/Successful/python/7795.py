# 7795
import sys
input = sys.stdin.readline
for _ in range(int(input().strip())) :
    n, m = map(int, input().strip().split())
    a = list(map(int, input().strip().split()))
    b = list(map(int, input().strip().split()))
    a.sort(reverse=True)
    b.sort(reverse=True)
    ai = bi = 0
    r = [0]*n
    while bi < m and ai < n:
        if a[ai] <= b[bi] : bi+=1
        else :
            r[ai] = max(m-bi, r[ai])
            ai += 1
    print(sum(r))
        # 8 7 3 1 1
        # 6 3 1

