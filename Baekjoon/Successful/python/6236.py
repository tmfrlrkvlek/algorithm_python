# 6236
import sys
input = sys.stdin.readline
n, m = map(int, input().strip().split())
days = [int(input().strip()) for _ in range(n)]
l = 0; r = 10000*n
def count(mid) :
    count = 1
    money = mid
    for day in days :
        if day <= money : money -= day
        else :
            money = mid - day
            count += 1
            if money < 0 : return n+1
    return count
result = 0
while l <= r :
    k = (l+r)//2
    cnt = count(k)
    if cnt <= m :
        result = k
        r = k-1
    else : l = k+1
print(result)