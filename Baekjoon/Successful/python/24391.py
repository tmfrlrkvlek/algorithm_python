# 24391
import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())
school_map = {i: [] for i in range(1, N+1)}
room_group = {i: 0 for i in range(1, N+1)}
for _ in range(M) :
    i, j = map(int, input().strip().split())
    school_map[i].append(j)
    school_map[j].append(i)

for start in range(1, N+1) :
    if room_group[start] != 0 :
        continue
    queue = [start]
    while queue :
        c = queue.pop()
        if room_group[c] != 0 :
            continue
        room_group[c] = start
        [queue.append(n) for n in school_map[c] if room_group[n] == 0]

answer = 0
timeline = list(map(int, input().strip().split()))
c = timeline[0]
for l in timeline[1:] :
    if room_group[c] != room_group[l] :
        answer += 1
    c = l
print(answer)