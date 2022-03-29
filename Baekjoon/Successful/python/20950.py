# 20950
import sys

input = sys.stdin.readline
N = int(input().strip())
RGBs = [list(map(int, input().strip().split())) for _ in range(N)]
Goal = list(map(int, input().strip().split()))

def diff(cur, count) :
    return sum([abs(Goal[0] - cur[0]//count), abs(Goal[1] - cur[1]//count), abs(Goal[2] - cur[2]//count)])

def add(cur, color) : 
    return [cur[0]+color[0], cur[1]+color[1], cur[2]+color[2]]

def test(cur, k, count) :
    if count == 7 : return diff(cur, count)
    minDiff = diff(cur, count)
    for i in range(k+1, N) :
        minDiff = min(test(add(cur, RGBs[i]), i, count+1), minDiff)
    return minDiff

result = float('inf')
for i in range(N) :
    for j in range(i+1, N) :
        result = min(test(add(RGBs[i], RGBs[j]), j, 2), result)
    
print(result)

# solution 2
# def add(cur, color) : 
#     return [cur[0]+color[0], cur[1]+color[1], cur[2]+color[2]]

# def diff(cur, count) :
#     return sum([abs(gom[0] - cur[0]//count), abs(gom[1] - cur[1]//count), abs(gom[2] - cur[2]//count)])

# def solution(rgb, m, num):
#     answer = float('inf') if num < 2 else diff(rgb, num)
#     for i in range(m+1, n):
#         if num < 7 : answer = min(solution(add(rgb, arr[i]), i, num+1), answer) 

#     return answer

# n = int(input())
# arr = [[*map(int, input().split())] for _ in range(n)]
# gom = [*map(int, input().split())]
# answer = solution([0,0,0], -1, 0)
# print(answer)
