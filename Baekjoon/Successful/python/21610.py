# 21610
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
a = [list(map(int, input().strip().split())) for _ in range(n)]
status = [[False] * n for _ in range(n)]
status[n-1][0:2] = [True, True]
status[n-2][0:2] = [True, True]
for _ in range(m) :
    d, c = map(int, input().strip().split())
    c %= n
    if d in [1, 2, 8]:  
        for i in range(n) : status[i] = status[i][c:] + status[i][:c]
    if d in [2, 3, 4] :
        status = status[c:] + status[:c]
    if d in [4, 5, 6] :
        for i in range(n) : status[i] = status[i][n-c:] + status[i][:n-c]
    if d in [6, 7, 8] :
        status = status[n-c:] + status[:n-c]
    for i in range(n) :
        for j in range(n) :
            if status[i][j] : a[i][j] += 1
    for i in range(n) :
        for j in range(n) :
            if status[i][j] :
                count = 0
                if i > 0 :
                    if j > 0 and a[i-1][j-1] > 0 : count += 1
                    if j < n-1 and a[i-1][j+1] > 0 :count += 1
                if i < n-1 :
                    if j > 0 and a[i+1][j-1] > 0 : count += 1
                    if j < n-1 and a[i+1][j+1] > 0 :count += 1
                a[i][j] += count
    for i in range(n) :
        for j in range(n) :
            if status[i][j] : status[i][j] = False
            elif a[i][j] >= 2 : 
                a[i][j] -= 2
                status[i][j] = True
print(sum(sum(a, [])))
