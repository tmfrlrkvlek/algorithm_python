# 1068

def dfs(tree , dn):
	deletenode = []
	stack = []
	stack.append(dn)
	while(stack) :
		dn = stack.pop(0)
		if dn not in deletenode : 
			deletenode.append(dn)
			for ch in tree[dn]:
				if ch not in deletenode : stack.append(ch)
	deletenode.sort(reverse=True)
	for dn in deletenode : del tree[dn]
	return tree

def countLeaf(tree, dn):
	sum = 0
	for leaf in tree:
		if leaf.count(dn) > 0 : leaf.remove(dn)
		if len(leaf) == 0: sum += 1
	return sum

n = int(input())
val = list(map(int, input().split()))
tree = [[] for _ in range(n)]
root = 0
for i in range(n):
	if val[i] == -1:
		root = i
	else :
		tree[val[i]].append(i)
dn = int(input())
print(countLeaf(dfs(tree, dn), dn))

