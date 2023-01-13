# 10707
import sys
input = sys.stdin.readline
X = int(input().strip())
Y = [int(input().strip()) for _ in range(3)]
JOI = int(input().strip())
print(min(X*JOI, Y[0]+(max(0, JOI-Y[1])*Y[2])))