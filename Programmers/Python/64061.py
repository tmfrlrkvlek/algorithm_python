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

