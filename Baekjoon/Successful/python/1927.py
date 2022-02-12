# 1927
import sys, heapq
input = sys.stdin.readline
arr = []
for _ in range(int(input().strip())) :
    num = int(input().strip())
    if num == 0:
        if arr : print(heapq.heappop(arr))
        else : print("0")
    else : heapq.heappush(arr, num)

