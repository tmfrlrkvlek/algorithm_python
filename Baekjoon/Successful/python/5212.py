# 5212
import sys
input = sys.stdin.readline
r, c = map(int, input().strip().split())
m = [list(input().strip()) for _ in range(r)]
nm = []
minx = r-1
maxx = 0
miny = c-1
maxy = 0
for x in range(r) :
    nl = []
    for y in range(c) :
        if m[x][y] == '.' : nl.append('.')
        else :
            count = 0
            if x == 0 : count += 1
            elif m[x-1][y] == '.' : count += 1
            if y == 0 : count += 1
            elif m[x][y-1] == '.' : count += 1
            if x == r-1 : count += 1
            elif m[x+1][y] == '.' : count += 1
            if y == c-1 : count += 1
            elif m[x][y+1] == '.' : count += 1
            if count >= 3 : nl.append('.')
            else : 
                nl.append('X')
                minx = min(minx, x)
                maxx = max(maxx, x+1)
                miny = min(miny, y)
                maxy = max(maxy, y+1)
    nm.append(nl)
for x in range(minx, maxx) :
    for y in range(miny, maxy) :
        print(nm[x][y], end="")
    print()