# 13900
import sys
input = sys.stdin.readline
N = int(input().strip())
Ints = list(map(int, input().strip().split()))
result = 0
total = sum(Ints)
for c in Ints : 
    total -= c
    result += c*total
print(result)
