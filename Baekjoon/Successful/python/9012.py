# 9012
import sys
input = sys.stdin.readline
t = int(input().strip())
for _ in range(t) :
    string = input().strip()
    cnt = 0
    for c in string :
        if c == '(' : cnt += 1
        else : cnt -= 1
        if cnt < 0 : break
    print("NO" if cnt else "YES")
