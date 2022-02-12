# 1158
import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())
person = [p for p in range(1, n+1)]
idx = 0
print("<", end="")
for _ in range(n) :
    idx = (idx+k-1)%len(person)
    p = person.pop(idx)
    if person : print(p, end=", ")
    else : print(p, end="")
print(">")