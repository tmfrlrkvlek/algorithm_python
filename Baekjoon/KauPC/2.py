import sys
input = sys.stdin.readline
day = 0
n, k, a, b = map(int, input().split())
b -= 1
ts = [k for _ in range(n)]
while True :
    ts.sort()
    if ts[0] == 0 : break
    day += 1
    for i in range(a): ts[i] += (b)
    for i in range(a, n) : ts[i] -= 1
print(day)