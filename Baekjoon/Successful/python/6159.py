import sys
input = sys.stdin.readline
N, S = map(int, input().rstrip().split())
L = sorted([int(input().rstrip()) for _ in range(N)])
result = 0
for i in range(N-1) :
    for j in range(i+1, N) :
        if L[i]+L[j] > S : break
        else : result += 1
print(result)