# 17943
import sys
input = sys.stdin.readline
N, Q = map(int, input().strip().split())
history = list(map(int, input().strip().split()))
dp = [0b0]
for h in history :
    dp.append(dp[-1]^h)

def q1(x, y, dp) :
    return dp[x]^dp[y]

def q2(x, y, d, dp) :
    return d ^ q1(x, y, dp)

for _ in range(Q) :
    q = list(map(int, input().strip().split()))
    if q[0] == 0:
        print(int(q1(q[1]-1, q[2]-1, dp)))
    else :
        print(int(q2(q[1]-1, q[2]-1, q[3], dp)))