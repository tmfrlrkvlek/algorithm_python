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

def solution2(board, moves):
    c = [0] * len(board)
    stack = []
    for row in moves :
        col = c[row-1]
        while col < len(board) and board[col][row-1] == 0 :
            col += 1
        c[row-1] = col
        if col == len(board) : 
            continue
        else :
            stack.append(board[col][row-1])
            board[col][row-1] = 0
    idx = 1
    cnt = 0
    while idx < len(stack) :
        if idx == 0 :
            idx += 1
        elif stack[idx] == stack[idx-1] :
            del stack[idx]; del stack[idx-1]
            cnt += 2; idx -= 1
        else :
            idx += 1
    return cnt