def solution(board):
    n = len(board)
    nums = set()
    locs = {k: [] for k in range(1, 201)}
    for i in range(n): 
        for j in range(n) :
            if board[i][j] == 0 :
                continue
            nums.add(board[i][j])
            locs[board[i][j]].append((i, j))
    cnt = 0
    order = []
    for num in nums :
        x1, _, x2, _ = minrect(locs[num], n)
        order.append((x1, x2, num))
    order.sort()
    order = [o[2] for o in order]
    for num in order :
        x1, y1, x2, y2 = minrect(locs[num], n)
        removable = True
        for i in range(x1, x2+1) :
            for j in range(y1, y2+1) :
                if board[i][j] == num :
                    continue
                elif not settle(i, j, board) :
                    removable = False
            if not removable: break
        if removable:
            cnt += 1
            for x, y in locs[num] :
                board[x][y] = 0
    return cnt

def minrect(locs, n) :
    minx = locs[0][0]
    maxx = locs[-1][0]
    miny, maxy = (n-1, 0)
    for _, y in locs :
        miny = min(miny, y)
        maxy = max(maxy, y)
    return (minx, miny, maxx, maxy)

def settle(x, y, board) :
    return not len([True for a in board[:x+1] if a[y] != 0])