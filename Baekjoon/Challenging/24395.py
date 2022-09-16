# 24395
# fail
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
diseases = [list(map(int, input().strip().split())) for _ in range(M)]
available_cases = [[-1] * (50*M+1) for _ in range((50*M+1))]

def find(current, D, red, blue):
    if current != -1 and available_cases[red][blue] < D :
        available_cases[red][blue] = D
    if current+1 == M :
        return
    r, b, d = diseases[current+1]
    find(current+1, D+d, red+r, blue+b)
    find(current+1, D, red, blue)
find(-1, 0, 0, 0)

student_list = []
for i in range(N) :
    r, b = map(int, input().strip().split())
    D = max(0, available_cases[r][b])
    student_list.append((D, i+1))
student_list.sort()

[print(num, d) for d, num in student_list]