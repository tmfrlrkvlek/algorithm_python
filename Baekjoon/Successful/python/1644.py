# 1644
import sys
n = int(sys.stdin.readline())

def primeArray(n) :
    pl = [True]*(n+1)
    for i in range(2, n+1) :
        if not pl[i] : continue
        else :
            for j in range(i*2, n+1, i) : pl[j] = False
    return [i for i in range(2, n+1) if pl[i]]

if n < 2 : print(0); exit(0)
pl = primeArray(n)
l = r = c = result = 0
s = pl[0]
maxr = len(pl)
while r < maxr :
    if s >= n : 
        if s == n : result += 1
        s -= pl[l]
        l += 1
    else :
        r += 1
        if r < maxr : s += pl[r]
print(result)    

