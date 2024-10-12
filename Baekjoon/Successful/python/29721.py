# 29721

N, K = map(int, input().split())
chessboard = set()
count = 0
for _ in range(K) :
    x, y = map(int, input().split())
    if (x-1, y-1) in chessboard :
        count -= 1
    chessboard.add((x-1, y-1))
    for (x1, y1) in [(-2, 0), (0, 2), (2, 0), (0, -2)]:
        if 0 < x+x1 <= N and 0 < y+y1 <= N and (x+x1-1, y+y1-1) not in chessboard:
            chessboard.add((x+x1-1, y+y1-1))
            count += 1
print(count)