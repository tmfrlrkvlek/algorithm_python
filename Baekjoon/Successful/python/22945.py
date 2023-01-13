# 22945

N = int(input())
x = list(map(int, input().split()))
def score(a, b) -> int :
    return min(x[a], x[b]) * (b-a-1)
i = 0
j = N-1
result = 0
while i < j :
    result = max(score(i, j), result)
    if x[j] > x[i] :
        i += 1
    else :
        j -= 1
print(result)
