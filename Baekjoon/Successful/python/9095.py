# 9095
import sys
input = sys.stdin.readline

facs = [1, 1] + [0]*10
def factorial(a) :
    if facs[a] > 0 : return facs[a]
    else : 
        facs[a] = a * factorial(a-1)
        return facs[a]

for _ in range(int(input().strip())) :
    N = int(input().strip())
    count = 0
    for c3 in range(N//3+1) :
        for c2 in range((N-c3*3)//2+1) :
            c1 = N - c3*3 - c2*2
            count += (factorial(c1+c2+c3) // (factorial(c1)*factorial(c2)*factorial(c3)))
    print(count)