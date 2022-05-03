from collections import deque
from itertools import permutations as pm

def solution(board, r, c):
    
    def ctrl_move(x, y, direction) :
        if direction == 0 :
            for i in range(y+1, 3) :
                if board[x][i] != 0 : return (x, i)
            return (x, 3)
        elif direction == 1 :
            for i in range(x-1, 0, -1) :
                if board[i][y] != 0 : return (i, y)
            return (0, y)
        elif direction == 2 :
            for i in range(y-1, 0, -1) :
                if board[x][i] != 0 : return (x, i)
            return (x, 0)
        else :
            for i in range(x+1, 3) :
                if board[i][y] != 0 : return (i, y)
            return (3, y)
    
    def cursor_move(x, y, direction) :
        if direction == 0 :
            return (x, max(0, y-1))
        elif direction == 1 :
            return (max(0, x-1), y)
        elif direction == 2 :
            return (x, min(3, y+1))
        else :
            return (min(3, x+1), y)
    
    def find_pair() :
        pairs = []
        [[pairs.append((board[i][j], i, j)) for i in range(4) if board[i][j] != 0] for j in range(4)]
        result = []
        pairs.sort()
        while pairs :
            _, fx, fy = pairs.pop()
            _, sx, sy = pairs.pop()
            result.append([(fx, fy), (sx, sy)])
        return result
    
    def distance(s, e) :
        x, y = s
        visited = [[False] * 4 for _ in range(4)]
        queue = deque([(0, x, y)])
        while queue :
            d, cx, cy = queue.popleft()
            if visited[cx][cy] : continue
            elif (cx, cy) == e : return d
            visited[cx][cy] = True
            [queue.append((d+1, a, b)) for a, b in sum([[cursor_move(cx, cy, i), ctrl_move(cx, cy, i)] for i in range(4)], []) if not visited[a][b]]
                
    def solve(r, c) :
        
        def move(order, c) :
            if not order : return 0
            dist = float('inf')
            for a, b in [(0, 1), (1, 0)] :
                c1, c2 = pairs[order[0]][a], pairs[order[0]][b]
                card = board[c1[0]][c1[1]]
                
                d = distance(c, c1) + 1
                board[c1[0]][c1[1]] = 0
                d += distance(c1, c2) + 1
                board[c2[0]][c2[1]] = 0
                d += move(order[1:], c2)

                board[c1[0]][c1[1]] = card
                board[c2[0]][c2[1]] = card

                dist = min(dist, d)
            return dist
        
        pairs = find_pair()
        result = float('inf')
        for combi in pm(range(len(pairs))) :
            result = min(result, move(combi, (r, c)))
        return result
    
    return solve(r, c)