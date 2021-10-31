# n 짝수
from itertools import combinations, permutations
import sys
input = sys.stdin.readline

n = int(input())
ss = [list(map(int, input().split())) for _ in range(n)]
diff = []

def sum(l) -> int :
    s = 0
    for x, y in l: s += ss[x][y]
    return s

for t1 in list(combinations(range(n), n//2)):
    t2 = [i for i in range(n) if i not in t1]
    s1, s2 = sum(list(permutations(t1, 2))), sum(list(permutations(t2, 2)))
    diff.append(abs(s1-s2))
print(min(diff))
