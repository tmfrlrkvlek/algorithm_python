# 1476
import sys
input = sys.stdin.readline

e, s, m = (1, 1, 1)
year = 1
E, S, M = map(int, input().strip().split())
E %= 15
S %= 28
M %= 19
while not (e == E and s == S and m == M) :
    year += 1
    e = (e+1)%15
    s = (s+1)%28
    m = (m+1)%19
print(year)