# 1931
import sys
input = sys.stdin.readline
N = int(input().strip())
queue = []
maxEndTime = 0
for _ in range(N) :
    s, e = map(int, input().strip().split())
    queue.append((s, e))
    maxEndTime = max(maxEndTime, e)
queue.sort(key=lambda x: (x[1], x[0]))

result = 0
before = (-1, -1)
while queue :
    current = queue.pop(0)
    if before[1] <= current[0] : 
        result += 1
        before = current
        
print(result)
