# 21608
import sys
input = sys.stdin.readline
n = int(input().strip())
a = [list(map(int,input().strip().split())) for _ in range(n*n)]
pa = []
seat = [[0] * n for _ in range(n)]

def findSat(i, j, likest) :
    near = []
    cl = [i > 0, j > 0, i < n-1, j < n-1]
    if cl[0] : near.append(seat[i-1][j])
    if cl[1] : near.append(seat[i][j-1])
    if cl[3] : near.append(seat[i][j+1])
    if cl[2] : near.append(seat[i+1][j])
    emptyCnt = near.count(0)
    if emptyCnt > 0 : near.remove(0)
    count = 0
    for p in near :
        if p in likest : count += 1
    return emptyCnt, count

def findNear(likest) :
    pos = []
    maxV = 0
    empty = []
    for i in range(n) :
        line = []
        for j in range(n) :
            if seat[i][j] != 0 : 
                line.append(0)
                continue
            emptyCnt, count = findSat(i, j, likest)
            line.append(emptyCnt)
            if maxV <= count :
                if maxV < count : 
                    pos = []
                    maxV = count
                pos.append((i,j))
        empty.append(line)
    return maxV, pos, empty

for s in a :
    _, pos, empty = findNear(s[1:])
    position = pos[0]
    if len(pos) > 1 :
        maxE = 0
        emptyPos = []
        for p in pos :
            if maxE <= empty[p[0]][p[1]] :
                if maxE < empty[p[0]][p[1]] :
                    maxE = empty[p[0]][p[1]]
                    emptyPos = []
                emptyPos.append(p)
        position = emptyPos[0]
    seat[position[0]][position[1]] = s[0]
    pa.append(position)

sat = 0
for i, s in enumerate(a) :
    _, maxV= findSat(pa[i][0], pa[i][1], s[1:])
    satP = [0, 1, 10, 100, 1000]
    sat += satP[maxV]

print(sat)
