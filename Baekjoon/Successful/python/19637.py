# 19637
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
titles = []
for _ in range(N) :
    title, max_num = map(str, input().strip().split())
    max_num = int(max_num)
    if len(titles) > 0 and max_num == titles[-1][0] :
        continue
    else :
        titles.append((max_num, title))
        
def find_title(ability) :
    left = 0
    right = len(titles)
    cur = int((left+right) / 2)
    while left < right :
        if ability <= titles[cur][0] :
            right = cur
        else :
            left = cur + 1
        cur = int((left+right) / 2)
    return titles[cur][1]
            
for _ in range(M):
    ability = int(input())
    print(find_title(ability))