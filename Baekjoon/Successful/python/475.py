# 475
import sys
input = sys.stdin.readline

N = int(input().strip())
chart = list(map(int, input().strip().split()))
answer = 0
max_price = chart.pop()
for p in chart.__reversed__() :
    answer += max(0, max_price-p)
    max_price = max(max_price, p)
print(answer)