# 1697
import sys
input = sys.stdin.readline
n, k = map(int, input().strip().split())

def bfs(n, k) :
    maxD = max(n, k)*2+1
    d = [maxD] * maxD
    v = [False] * maxD
    q = [n]
    d[n] = 0
    while q:
        node = q.pop(0)
        if v[node] : continue
        elif node == k : return d[k]
        v[node] = True
        if 0 <= node-1 :
            q.append(node-1)
            d[node-1] = min(d[node-1], d[node]+1)
        if 0 <= node+1 < maxD : 
            q.append(node+1)
            d[node+1] = min(d[node+1], d[node]+1)
        if 0 <= node*2 < maxD : 
            q.append(node*2)
            d[node*2] = min(d[node*2], d[node]+1)
        
print(bfs(n, k))