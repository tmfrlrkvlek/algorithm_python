# 2493.py

# stack

t = int(input())
tops = list(map(int, input().split(' ')))
stack = []
answer = [0] * t
for i in range(t):
    h = tops[i]
    while stack and stack[-1][0] < h:
        stack.pop()
    if stack:
        answer[i] = stack[-1][1] + 1
    stack.append([h,i])
print(' '.join(list(map(str, answer))))