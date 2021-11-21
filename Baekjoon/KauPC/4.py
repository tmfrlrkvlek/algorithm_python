import sys
input = sys.stdin.readline

n = int(input())
b = [list(map(int, input().split())) for _ in range(n)]

def score(i, j) -> int:
    score = 0
    s1 = 1
    if i == j or n-i-1 == j :
        if i == j or i == n//2 + 1:
            for k in range(i-1, -1, -1):
                if b[k][k] == 1 : s1 += 1
                else: break
            for k in range(i+1, n):
                if b[k][k] == 1 : s1 += 1
                else: break
        if n-i == j or i == n//2 + 1:
            for k in range(i-1, -1, -1):
                if b[n-k-1][k] == 1 : s1 += 1
                else: break
            for k in range(i+1, n):
                if b[n-k-1][k] == 1 : s1 += 1
                else: break
        score = s1
    s1 = 1
    for k in range(i-1, -1, -1):
        if b[k][j] == 1 : s1 += 1
        else: break
    for k in range(i+1, n):
        if b[k][j] == 1 : s1 += 1
        else: break
    score = s1 if score < s1 else score
    s1 = 1
    for k in range(j-1, -1, -1):
        if b[i][k] == 1 : s1 += 1
        else: break
    for k in range(j+1, n):
        if b[i][k] == 1 : s1 += 1
        else: break
    score = s1 if score < s1 else score
    return score
maxS = 0
for i in range(n):
    for j in range(n):
        if j != 0 :
            sc = score(i, j)
            maxS = sc if sc > maxS else maxS
print(maxS)
