# 2869
import sys
input = sys.stdin.readline
a, b, v = map(int, input().split())
d = (v-b)/(a-b)
print(int(d+1) if d%1!=0 else int(d))
