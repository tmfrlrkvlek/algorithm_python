# 17179
import sys
input = sys.stdin.readline

def slice(mid) :
    count = 0
    remain = s[0]
    minslice = s[-1]
    for i in range(m+1) :
        if i : remain += (s[i]-s[i-1])
        if remain >= mid :
            minslice = min(remain, minslice)
            remain = 0
            count += 1
    return count, minslice

n, m, length = map(int, input().strip().split())
s = [int(input().strip()) for _ in range(m)] + [length]

for _ in range(n) :
    q = int(input().strip())
    l = 0; r = s[-1]
    result = 0
    while l <= r :
        lg = (l+r)//2
        count, minS = slice(lg)
        if count > q : 
            result = max(minS, result)
            l = lg+1
        else : r = lg-1
    print(result)


