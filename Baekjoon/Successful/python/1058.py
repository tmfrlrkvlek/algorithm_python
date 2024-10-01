n = int(input())
friends = [[] for _ in range(n)]
for me in range(n):
    relation = input()
    for friend in range(n) :
        if relation[friend] == 'Y' :
            friends[me] += [friend]
result = 1
for person in range(n) :
    two_friend = set(friends[person])
    for friend in friends[person]:
        two_friend.update(friends[friend])
    result = max(result, len(two_friend))
print(result - 1)