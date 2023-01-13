# 2668
import sys
input = sys.stdin.readline
N = int(input())
graph = {idx : [] for idx in range(1, N+1)}

for idx in range(1, N+1) :
    num = int(input())
    graph[num].append(idx)

def solve(cur, visited, root, cnt, result) :
    if len(graph[cur]) == 0 :
        return result, -1
    elif visited[cur] and cur == root:
        return result[:-1], cnt-1
    visited[cur] = True
    r_result, r_cnt = solve(graph[cur][0], visited, root, cnt+1, result+[graph[cur][0]]) 
    for i in graph[cur] :
        if i == graph[cur][0] : continue
        a_result, a_cnt = solve(i, visited, root, cnt+1, result+[i]) 
        if r_cnt < a_cnt :
            r_cnt = a_cnt
            r_result = a_result
    return r_result, r_cnt

visited = [False for _ in range(N+1)]
result = []
for i in range(1, N+1) :
    if len(graph[i]) == 0 or visited[i]: continue
    res, cnt = solve(i, [False for i in range(N+1)], i, 1, [i])
    if cnt > 0 :
        result.extend(res)
    for k in res :
        visited[k] = True
print(len(result))
[print(i) for i in sorted(result)]
# 3 - 1
# 1 - 2, 3
# 5 - 4, 5
# 4 - 6
# 6 - 7
