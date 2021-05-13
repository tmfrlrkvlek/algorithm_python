# 1547

m = int(input())
loc = [1, 2, 3]

for i in range(m):
    # x, y = map(int,input().split())
    x, y = input().split()
    x = int(x)
    y = int(y)
    # x 인덱스 찾기
    xidx = 0
    for xidx in range(3):
        if loc[xidx] == x:
            break
    # y 인덱스 찾기
    yidx = 0
    for yidx in range(3):
        if loc[yidx] == y:
            break
    loc[xidx] = y
    loc[yidx] = x
    
print(loc[0])

# 간단하게 하면..

# m = int(input())

# for i in range(m):
#     x, y = map(int,input().split())
#     xidx = loc.index(x)
#     yidx = loc.index(y)
#     loc[xidx] = y
#     loc[yidx] = x
# print(loc[0])