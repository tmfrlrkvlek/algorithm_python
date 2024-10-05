# 2716

t = int(input())

def solve(tree) :
    maxDepth = 0
    currentDepth = 0
    for i in tree :
        if i == '[' :
            currentDepth += 1
        else :
            currentDepth -= 1
        maxDepth = max(currentDepth, maxDepth)
    return 2**maxDepth

for _ in range(t) :
    tree = input()
    print(solve(tree))
    