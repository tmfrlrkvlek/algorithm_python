# 25186
N = int(input())
D = list(map(int, input().split()))
maxCnt = max(D)
sumValue = 0
if N == 1 :
    print("Happy" if D[0] == 1 else "Unhappy")
else :
    for i in range(N) :
        if sumValue < 10**6 :
            sumValue += D[i]
        else :
            break
        if D[i] > maxCnt : 
            maxCnt = D[i]
    if maxCnt > (sumValue//2) :
        print("Unhappy")
    else :
        print("Happy")