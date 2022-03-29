# 16509
import sys
from collections import deque
input = sys.stdin.readline
board = [[float('inf')] * 9 for _ in range(10)]
r1, c1 = map(int, input().strip().split())
kr, kc = map(int, input().strip().split())
board[r1][c1] = 0

def check(c, diff) :
    cr, cc = c
    a, b = (0, 1 if diff[1] > 0 else -1) if abs(diff[0]) < abs(diff[1]) else (1 if diff[0] > 0 else -1, 0)
    cr, cc = cr+a, cc+b
    if cr == kr and cc == kc : return False
    a, b = (diff[0]-a)//2, (diff[1]-b)//2
    if cr+a == kr and cc+b == kc : return False
    else : return True


queue = deque([(r1, c1, 0)])
while queue :
    r, c, dist = queue.popleft()
    if board[r][c] < dist : continue
    for (a, b) in [(-3, 2), (-2, 3), (2, 3), (3, 2), (3, -2), (2, -3), (-2, -3), (-3, -2)] :
        nr, nc = r+a, c+b
        if not (0 <= nr < 10 and 0 <= nc < 9) : continue
        elif board[nr][nc] <= dist+1 : continue
        elif check((r, c), (a, b)): 
            board[nr][nc] = dist+1
            queue.append((nr, nc, dist+1))

print(board[kr][kc] if board[kr][kc] < float('inf') else -1)