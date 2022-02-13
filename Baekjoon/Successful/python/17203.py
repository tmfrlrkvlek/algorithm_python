# 17203
import sys
input = sys.stdin.readline
n, q = map(int, input().strip().split())
A = list(map(int, input().strip().split()))

def diff(i, j) :
    if j-1 < i : return 0
    result = 0
    for k in range(i-1, j-1) : result += abs(A[k+1]-A[k])
    return result

for _ in range(q):
    i, j = map(int, input().strip().split())
    print(diff(i, j))
