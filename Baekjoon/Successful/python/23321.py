# 23321
import sys
input = sys.stdin.readline
rule = [[".","o"],["o","w"],["l","m"],["l","n"],[".","n"]]
sm = [input().rstrip() for _ in range(5)]
sit = [i for i, k in enumerate(sm[1]) if k == "."]
for i, c in enumerate(sm) :
    for j, item in enumerate(c) :
        if j in sit : print(item,end="")
        else : print(rule[i][0] if rule[i][0] != item else rule[i][1],end="")
    print()