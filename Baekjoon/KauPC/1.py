# 3번
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
p = []; w = []
for _ in range(n) :
    p1, w1 = map(int, input().split())
    p.append(p1); w.append(w1)
cost = 0
ap = [m+1]; aw = [1]
while p :
    p1 = ap[-1]; w1=aw[-1]; p2 = p.pop(0); w2 = w.pop(0)
    print(p1, w1, p2, w2)
    while (p2==p1 and w2>w1) or p1>p2+1 or p1<p2:
        if p1>p2+1 : 
            cost += w2
            p.append(p2); w.append(w2)
            p2 = p.pop(0); w2 = w.pop(0)
        elif (p2==p1 and w2>w1) or p1<p2 :
            cost += w1
            p.append(p1); w.append(w1);
            ap.pop(); aw.pop()
            if not ap : break
            p1 = ap[-1]; w1=aw[-1]
        print(cost)
    # cost += w2
    print(cost)
    ap.append(p2); aw.append(w2)
print(cost)
