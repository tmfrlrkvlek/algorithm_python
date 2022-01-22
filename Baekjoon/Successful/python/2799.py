# 2799
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
count = [0, 0, 0, 0, 0]
for _ in range(n) :
    input().rstrip()
    line = [0] * m
    for _ in range(4) :
        l = input().rstrip()
        for j in range(m) :
            if l[1 + j*5] == '*' : line[j] += 1
    for k in line :
        count[k] += 1

input().rstrip()
for i in count : print(i, end=" ")
