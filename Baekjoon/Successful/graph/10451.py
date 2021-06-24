# 10451

def checkTotal(graph, n):
	visit = [False] * len(graph)
	total = 0
	for startnode in range(1, n+1) :
		if visit[startnode]:
			continue
		total += 1
		visit[startnode] = True
		node = graph[startnode]
		while not visit[node]:
			visit[node] = True
			node = graph[node]
	return total
			
t = int(input())
for k in range(t):
	n = int(input())
	graph = [0] + list(map(int, input().split()))
	print(checkTotal(graph, n))
