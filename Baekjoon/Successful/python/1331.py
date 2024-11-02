# 1331

visited = [[False] * 6 for _ in range(6)]

def knight_can_go(prev, cur) :
    row_gap = abs(ord(prev[0]) - ord(cur[0]))
    col_gap = abs(int(prev[1]) - int(cur[1]))
    return row_gap * col_gap == 2

def calculate_row(cur) :
    return ord(cur[0]) - 65

def calculate_column(cur) :
    return int(cur[1]) - 1

prev = input()
start = prev
cur = ''
visited[calculate_row(prev)][calculate_column(prev)] = True

answer = True
for _ in range(35) :
    cur = input()
    row = calculate_row(cur)
    col = calculate_column(cur)
    if visited[row][col] == True :
        answer = False
    visited[row][col] = True
    if len(prev) > 0 and knight_can_go(prev, cur) == False :
        answer = False
    prev = cur

answer = answer and knight_can_go(start, cur)

print("Valid" if answer else "Invalid")