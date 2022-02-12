# 11279
import heapq, sys
input = sys.stdin.readline
n = int(input().strip())
arr = []
for _ in range(n) :
    num = int(input().strip())
    if num == 0 : 
        if arr : print(heapq.heappop(arr)[1])
        else : print("0")
    else : heapq.heappush(arr, (-num, num))



