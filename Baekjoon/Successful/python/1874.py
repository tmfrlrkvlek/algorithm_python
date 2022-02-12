# 1874
import sys
input = sys.stdin.readline
n = int(input().strip())
il = [int(input().strip()) for _ in range(n)]
stack = []; arr = []
for i in range(1, n+1):
    arr.append("+")
    if i == il[0] : 
        arr.append("-"); il.pop(0)
    else : stack.append(i)
    while stack and stack[-1] == il[0] :
        arr.append("-"); il.pop(0); stack.pop()
if il : print("NO")
else : 
    for c in arr : print(c)
    
    


