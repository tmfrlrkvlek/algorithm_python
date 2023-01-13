# 11582
import sys
input = sys.stdin.readline
N = int(input().strip())
Ts = list(map(int, input().strip().split()))
k = int(input().strip())

def sort(cnt: int) :
    mid = cnt // 2
    for i in range(0, N, cnt) :
        a = Ts[i:i+mid]
        b = Ts[i+mid:i+cnt]
        c = []
        a_idx = 0
        b_idx = 0
        for _ in range(0, cnt) :
            if a_idx >= mid or b_idx >= mid :
                break
            elif a[a_idx] <= b[b_idx] :
                c.append(a[a_idx])
                a_idx += 1
            else :
                c.append(b[b_idx])
                b_idx += 1
        [c.append(a[i]) for i in range(a_idx, mid)]
        [c.append(b[i]) for i in range(b_idx, mid)]
        Ts[i:i+cnt] = c
        
stride = 2

while True :
    sort(stride)
    if N//stride == k :
        [print(i, end=" ") for i in Ts]
        break
    stride *= 2
