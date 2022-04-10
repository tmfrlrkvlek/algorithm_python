# 1620
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
pocketmons = ['']+[input().strip() for _ in range(N)]
pocketmons2 = {}
for i in range(1, N+1) :
    pocketmons2[pocketmons[i]] = i
for _ in range(M) :
    key = input().strip()
    if 49 <= ord(key[0]) <= 57 :
        print(pocketmons[int(key)])
    else :
        print(pocketmons2[key])
