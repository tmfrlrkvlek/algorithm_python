# 16236
import sys
input = sys.stdin.readline

babyshark = 2
n = int(input().strip())
space = []
babyShartPos = (0, 0)
for x in range(n) :
    space.append(list(map(int, input().strip().split())))
    for y, f in enumerate(space[-1]) : 
        if f == 9 : 
            babyShartPos = (x, y)
            space[-1][y] = 0

def distance(start):
    q = [(start, 0)]
    visited = [[True]*n for _ in range(n)]
    fish = [[(-1, -1), n*n+1]]
    while len(q) :
        a = q.pop(0)
        if len(fish) > 1 and fish[-1][1] < a[1] : break 
        if 0 < space[a[0][0]][a[0][1]] < babyshark : fish.append(a)
        if not visited[a[0][0]][a[0][1]] or space[a[0][0]][a[0][1]] > babyshark : continue
        else : visited[a[0][0]][a[0][1]] = False
        if a[0][0] != 0 : q.append([(a[0][0]-1, a[0][1]), a[1]+1])
        if a[0][1] != 0 : q.append([(a[0][0], a[0][1]-1), a[1]+1])
        if a[0][0] != n-1 : q.append([(a[0][0]+1, a[0][1]), a[1]+1])
        if a[0][1] != n-1 : q.append([(a[0][0], a[0][1]+1), a[1]+1])
    fish.sort(key=lambda x: (x[1], x[0][0], x[0][1]))
    return fish[0]
    
time = 0
fishCount = 0
while True :
    result = distance(babyShartPos)
    if result[0][0] < 0 : break
    time += result[1]
    babyShartPos = result[0]
    fishCount += 1
    if fishCount == babyshark :
        babyshark += 1
        fishCount = 0
    space[babyShartPos[0]][babyShartPos[1]] = 0
print(time)


# 5 4 0 0 0 4
# 4 3 0 3 4 5
# 3 2 0 5 6 6
# 2 0 0 3 4 5
# 3 2 0 6 5 4
# 6 6 6 6 6 6

# time 12
# size 4
# count 2

