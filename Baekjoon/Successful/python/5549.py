# 5549
import sys
input = sys.stdin.readline
M, N = map(int, input().split())
K = int(input().strip())
contents = [input().strip() for _ in range(M)]
sums = [[0] * N for _ in range(M)]
for i in range(M) :
    d, e, f = 0, 0, 0
    for j in range(N) :
        a, b, c = sums[i-1][j] if i > 0 else (0, 0, 0)
        if contents[i][j] == "J" :
            sums[i][j] = (a+d+1, b+e, c+f)
            d += 1
        elif contents[i][j] == "O" :
            sums[i][j] = (a+d, b+e+1, c+f)
            e += 1
        elif contents[i][j] == "I" :
            sums[i][j] = (a+d, b+e, c+f+1)
            f += 1
        
for _ in range(K) :
    a, b, c, d = map(int, input().split())
    a-=1; b-=1; c-=1; d-=1
    r1, r2, r3 = sums[c][d]
    if a > 0 and b > 0 : 
        d1, d2, d3 = sums[a-1][b-1] 
        r1 += d1
        r2 += d2
        r3 += d3
    if a > 0 :
        d1, d2, d3 = sums[a-1][d]
        r1 -= d1
        r2 -= d2
        r3 -= d3
    if b > 0 :
        d1, d2, d3 = sums[c][b-1]
        r1 -= d1
        r2 -= d2
        r3 -= d3
    print(r1, r2 ,r3)

