import sys
input = sys.stdin.readline

T = int(input().strip())
for _ in range(T) :
    N = int(input().strip())
    A = list(map(int, input().strip().split()))
    M = int(input().strip())
    B = list(map(int, input().strip().split()))
    K = int(input().strip())
    C = list(map(int, input().strip().split()))
    result = set()
    [[[result.add(A[i]+B[j]+C[k]) for k in range(K) if set(str(A[i]+B[j]+C[k])) in [{'5'}, {'8'}, {'5', '8'}]] for j in range(M)] for i in range(N)]
    print(len(result))