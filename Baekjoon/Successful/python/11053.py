# 11053
import sys
input = sys.stdin.readline
n = int(input())
l = list(map(int, input().split()))
l2 = [0] * n
def find(num) :
    l2[num] = max([l2[i] + 1 for i in range(num) if l[i] < l[num]] + [1])
[find(i) for i in range(n)]
print(max(l2))

q = []
[q.append(l[i]) for i in range(n) if l[i] < q[-1]]

