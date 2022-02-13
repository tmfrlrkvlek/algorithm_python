# 1935
import sys
from collections import deque
input = sys.stdin.readline
n = int(input().strip())
string = input().strip()
var = [float(input().strip()) for _ in range(n)]
stack = deque()
for c in string :
    if 65 <= ord(c) <= 90 : 
        stack.append(var[ord(c)-65])
    else :
        n1 = stack.pop()
        n2 = stack.pop()
        if c == "+" : stack.append(n1+n2)
        elif c == "*" : stack.append(n1*n2)
        elif c == "/" : stack.append(n2/n1)
        elif c == "-" : stack.append(n2-n1)
print('%.2f' %(stack.pop()))