# 10216

# union-find algorithm

def find(target, parent):
    if target == parent[target]:
        return target
    parent[target] = find(parent[target], parent)
    return parent[target]

def union(a, b, parent):
    a = find(a, parent)
    b = find(b, parent)
    if(a == b): return
    else:
        if a < b:
            parent[b] = a
        else:
            parent[a] = b

t = int(input())
for test in range(t):
    t -= 1
    n = int(input())
    enemy = []
    parent = list(range(n))
    for i in range(n):
        enemy.append(list(map(int, input().split(' '))))
    for i in range(n):
        x1 = enemy[i][0]
        y1 = enemy[i][1]
        r1 = enemy[i][2]
        for j in range(i):
            if (x1 - enemy[j][0]) ** 2 + (y1 - enemy[j][1]) **2 <= (r1 + enemy[j][2]) ** 2 :
                    union(i, j, parent)
    for i in range(n):
        find(i, parent)
    print(len(set(parent)))