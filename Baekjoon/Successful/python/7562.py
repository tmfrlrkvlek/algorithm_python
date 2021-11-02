# 7562
import sys
input = sys.stdin.readline

def bfs(s, e, l) -> int:
    c = [[-1] * l for _ in range(l)]
    q = []
    q.append(s)
    c[s[0]][s[1]] = 0
    while q :
        cp = q.pop(0)
        available = [[cp[0]-2, cp[1]+1], [cp[0]-1, cp[1]+2], [cp[0]+1, cp[1]+2], [cp[0]+2, cp[1]+1], [cp[0]-2, cp[1]-1], [cp[0]-1, cp[1]-2], [cp[0]+1, cp[1]-2], [cp[0]+2, cp[1]-1]]
        depth = c[cp[0]][cp[1]] + 1
        for p in available:
            if 0<=p[0]<l and 0<=p[1]<l and c[p[0]][p[1]] == -1 :
                c[p[0]][p[1]] = depth
                q.append(p)
        if c[e[0]][e[1]] != -1: return c[e[0]][e[1]]

n = int(input())
for _ in range(n) :
    l = int(input())
    cx, cy = map(int, input().split())
    gx, gy = map(int, input().split())
    print(bfs([cx, cy], [gx, gy], l))