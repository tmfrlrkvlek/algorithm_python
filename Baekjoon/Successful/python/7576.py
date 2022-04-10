# 7576
import sys
from collections import deque
input = sys.stdin.readline
M, N = map(int, input().strip().split())
boxes = []
queue = deque()
for i in range(N) :
    boxes.append(list(map(int, input().strip().split())))
    for j in range(M) :
        if boxes[-1][j] == 1 : queue.append((i, j, 0))

def check() :
    for i in range(N) :
        for j in range(M) :
            if boxes[i][j] == 0 : return False
    return True

while queue :
    x, y, d = queue.popleft()
    for (i, j) in [(1, 0), (0, 1), (-1, 0), (0, -1)] :
        if 0 <= x+i < N and 0 <= y+j < M and boxes[x+i][y+j] == 0 :
            boxes[x+i][y+j] = 1
            queue.append((x+i, y+j, d+1))
print(d if check() else -1)
