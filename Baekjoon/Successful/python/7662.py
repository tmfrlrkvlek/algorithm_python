# 7662
import sys, heapq
input = sys.stdin.readline

for _ in range(int(input().strip())) :
    minq = []; maxq = []
    insert = 0; delete = 0
    heapq.heapify(minq)
    heapq.heapify(maxq)
    valid = {}
    for _ in range(int(input().strip())) :
        command, num = map(str, input().strip().split())
        num = int(num)
        if command == "I" :
            insert += 1
            if num in valid : valid[num] += 1
            else : valid[num] = 1
            heapq.heappush(minq, num)
            heapq.heappush(maxq, -num)
        elif insert > delete :
            if num == 1 : 
                key = -heapq.heappop(maxq)
                while not valid[key] : key = -heapq.heappop(maxq)
            else :  
                key = heapq.heappop(minq)
                while not valid[key] : key = heapq.heappop(minq)
            delete += 1
            valid[key] -= 1
    if insert-delete :
        minV = heapq.heappop(minq)
        while not valid[minV] : minV = heapq.heappop(minq)
        maxV = -heapq.heappop(maxq)
        while not valid[maxV] : maxV = -heapq.heappop(maxq)
        print(maxV, minV)
    else :
        print("EMPTY")

