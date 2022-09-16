# 24390
import sys
input = sys.stdin.readline

M, S = map(int, input().strip().split(':'))
goal = M*60+S

def count(goal) :
    cnt = goal//600
    goal %= 600
    cnt += goal//60
    goal %= 60
    cnt += max(0, goal//30-1)
    goal %= 30
    cnt += goal//10
    return cnt+1

print(count(goal))