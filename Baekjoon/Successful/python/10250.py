# 10250
import sys
input = sys.stdin.readline
for _ in range(int(input())) :
    h, w, n = map(int, input().split())
    r = n%h; s = n//h
    print("%d%02d" %(r if r else h, s if r==0 else s+1))
    