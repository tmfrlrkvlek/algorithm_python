# 1535
import sys
input = sys.stdin.readline

N = int(input().strip())
L = list(map(int, input().strip().split()))
J = list(map(int, input().strip().split()))

def recursive(cL, cJ, idx) :
    if idx == N : return cJ
    result = recursive(cL, cJ, idx+1)
    if cL > L[idx] : result = max(result, recursive(cL-L[idx], cJ+J[idx], idx+1))
    return result

print(recursive(100, 0, 0))