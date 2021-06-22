def dfs(graph, start_node) :
	visit = list()
	stack = list()

	stack.append(start_node) 

	while stack :
		node = stack.pop()
		if node not in visit :
			visit.append(node)
			stack.extend(graph[node])

	return visit

