# 24394
import sys
input = sys.stdin.readline

T = int(input().strip())
dp = [-1] * (10**9+20000)

def score(N, a, b, c) :
    good = (10**9)/(2*N)
    perfect = good*2+1
    great = good*2
    return int((10**9)*((2*perfect*a+2*great*b+good*c)/(2*N)) + perfect*a)

print(score(100, 10, 20, 30))