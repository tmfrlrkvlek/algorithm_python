# 1005
# 실패
import sys
input = sys.stdin.readline

def findRoute(orders, queue) :
    order = []
    while len(queue) :
        order.append(queue); queue = []
        for _, num in order[-1] :
            queue.append((num, orders[num]))
    return order

def minTime(n, times, orders, w) :
    order = findRoute(orders, [(None, w)])
    time = 0; visited = [-1] * n
    for step in reversed(order) :
        print(step)
        stepTime = [0]
        for _, b in step :
            visitList = [item for ia, item in orders[b] if (not visited[item]) or (ia != b)]
            if len(visitList) == 0 and times[b] > time : stepTime.append(times[b] - time)
            elif len(visitList) > 0 : stepTime.append(times[b])
            visited[b] = True
        time += max(stepTime)
    return time

def solution() :
    n, k = map(int, input().split())
    times = list(map(int, input().split()))
    orders = [[] for _ in range(n)]
    for _ in range(k) :
        s, e = map(int, input().split())
        orders[e-1].append(s-1)
    w = int(input())
    print(minTime(n, times, orders, w-1))

t = int(input())
[solution() for _ in range(t)]


