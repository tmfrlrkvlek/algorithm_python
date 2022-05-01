# 9372
import sys
input = sys.stdin.readline
for _ in range(int(input().strip())) :
    N, M = map(int, input().split())
    [input() for _ in range(M)]
    print(N-1)