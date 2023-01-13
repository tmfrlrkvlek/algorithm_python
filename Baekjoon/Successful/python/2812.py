# 2812
from collections import deque
N, K = map(int, input().split())
num = deque(list(map(int, list(input()))))
stack = [num.popleft()]
cnt = K
while cnt > 0 and num :
    a = num.popleft()
    while cnt > 0 and stack and stack[-1] < a :
        stack.pop()
        cnt -= 1
    stack.append(a)
stack.extend(num)
[print(stack[i], end="") for i in range(N-K)]


