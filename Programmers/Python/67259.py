import heapq

def solution(board):
    answer = 0
    n = len(board)
    costs = [[float('inf')] * n for i in range(n)]
    stack = [(0, 0, 0, 2)] 
    costs[0][0] = 0
    while stack :
        cost, x, y, dir = heapq.heappop(stack)
        if cost > costs[x][y] + 400 : continue
        available = [(-1, 0, 100), (1, 0, 100), (0, 1, 100), (0, -1, 100)]
        if dir == 1 :
            available = [(-1, 0, 100), (1, 0, 100), (0, 1, 600), (0, -1, 600)]
        elif dir == 0 :
            available = [(-1, 0, 600), (1, 0, 600), (0, 1, 100), (0, -1, 100)]
        for a, b, fee in available :
            if (not (0 <= x+a < n and 0 <= y+b < n)) or board[x+a][y+b] :
                continue
            if cost+fee <= costs[x+a][y+b] + 400 :
                costs[x+a][y+b] = min(cost+fee, costs[x+a][y+b])
                heapq.heappush(stack, (cost+fee, x+a, y+b, abs(a)))
    return costs[n-1][n-1]