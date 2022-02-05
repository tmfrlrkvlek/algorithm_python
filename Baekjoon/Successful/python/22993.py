# 22993
import sys
input = sys.stdin.readline

n = int(input().strip())
go = list(map(int,input().strip().split()))
jun = go[0]
go = sorted(go[1:])
win = True
for g in go :
    if jun <= g: 
        win = False
        break
    else : jun += g
print("Yes" if win else "No")