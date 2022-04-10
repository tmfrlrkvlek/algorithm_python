# 2630
import sys
input = sys.stdin.readline

N = int(input().strip())
square = [list(map(int, input().strip().split())) for _ in range(N)]

def check(p, r) :
    x, y = p
    isBlue = True
    isWhite = True
    for i in range(x, x+r) :
        for j in range(y, y+r) :
            if square[i][j] == 1 : isWhite = False
            else : isBlue = False
            if not (isWhite or isBlue) : return 2
    if isBlue : return 1
    elif isWhite : return 0
    else : return 2

def find(p, r) :
    whiteCount = 0
    blueCount = 0
    result = check(p, r)
    if result == 0 : whiteCount += 1
    elif result == 1 : blueCount += 1
    else :
        x, y = p
        r2 = r//2
        for i, j in [(0, 0), (0, r2), (r2, 0), (r2, r2)] :
            w, b = find((x+i, y+j), r2)
            whiteCount += w; blueCount += b
    return (whiteCount, blueCount)

w, b = find((0,0), N)
print(f'{w}\n{b}'.format(w, b))