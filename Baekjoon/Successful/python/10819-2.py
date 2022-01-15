# 10819-2

import sys, itertools
input = sys.stdin.readline
n = int(input().rstrip())
l = list(map(int, input().rstrip().split()))
m = 0
for p in itertools.permutations(l) :
    m = max(m, sum([abs(p[i-1]-p[i]) for i in range(1, n)]))
print(m)