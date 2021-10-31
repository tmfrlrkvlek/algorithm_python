# 15649
from itertools import permutations

n, m = map(int, input().split())
for c in list(permutations(range(1, n+1),m)):
    [print(e, end=" ") for e in c]
    print()
