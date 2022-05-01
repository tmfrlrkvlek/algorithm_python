# 10157
C, R = map(int, input().split())
K = int(input())
x, y = (1, 1)
up, left, down, right = (R-1, C-2, R-1, C-1)
for num in range(1, C*R+1):
    if num == K :
        print(y, x)
        exit(0)
    if up > 0 :
        up -= 1
        x += 1
    elif right > 0 :
        right -= 1
        y += 1
    elif down > 0 :
        down -= 1
        x -= 1
    elif left > 0 :
        left -= 1
        y -= 1
    else :
        x += 1
        R-=2; C-=2
        up, left, down, right = (R-1, C-2, R-1, C-1)
print(0)