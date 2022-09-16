# 17950
import sys
input = sys.stdin.readline
H, x = map(int, input().strip().split())
answer = 0
y = x
for k in range(1,H+1) :
    answer = (answer+int(input().strip())*y)%1000000007
    y=(y*x)%1000000007
print(answer)