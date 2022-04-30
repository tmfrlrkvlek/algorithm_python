def solution(board, moves):
    conv_board = [[] for _ in range(len(board))]
    [[conv_board[num].append(line[num]) for num in range(len(board)) if line[num] != 0] for line in board[::-1]]
    stack = []
    result = 0
    for move in moves :
        if conv_board[move-1] :
            doll = conv_board[move-1].pop()
            if stack and doll == stack[-1]:
                result += 2
                stack = stack[:-1]
            else :
                stack.append(doll)
    return result


import sys
input = sys.stdin.readline

def solution():
    _, m = map(int, input().split())
    times = [*map(int, input().split())]
    l, r = 0, 10**12
    result = 0
    while l < r:
        mid = (l+r) // 2
        if sum([mid//t for t in times]) < m:
            l = mid+1
        else:
            result = mid
            r = mid     
    print(result)
solution()