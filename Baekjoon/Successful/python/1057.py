# 1057

n, knum, inum = map(int, input().split())
round = 0
while (n > 0):
    round += 1
    knum = (knum + 1) // 2
    inum = (inum + 1) // 2
    if knum == inum :
        print(round)
        break
    n = (n % 2) + (n // 2)

if n <= 0:
    print(-1)