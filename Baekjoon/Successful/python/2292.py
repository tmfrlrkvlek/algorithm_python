# 2292
import sys
input = sys.stdin.readline
n = int(input())
if n == 1 : print(1)
else:
    d = (n-2)//6
    i = 2
    while d > 0:
        d -= i
        i += 1
    print(i)

