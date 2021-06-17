# 1034
import copy
from itertools import combinations_with_replacement

# 입력
n, m = map(int, input().split())
lamps = [] 
bingo = 0
for i in range(n):
	lamps.append(list(map(int, input())))
	if i not in lamps[i]:
		bingo += 1
k = int(input())

# 결과
def checkBingo(lists):
	global n
	bingo = 0
	for i in range(n):
		if 0 not in lists[i]: bingo += 1
	return bingo

def turnLamps(lists, cwr):
	global k
	i = 0
	while(i != k):
		ii = cwr[i]
		if cwr.count(ii) % 2 :
			for j in range(n) : lists[j][ii] = 0 if lists[j][ii] else 1
		i += (cwr.count(ii))
	return checkBingo(lists)

bingoList = []
for cwr in combinations_with_replacement(list(range(m)), k):
	bingoList.append(turnLamps(copy.deepcopy(lamps), cwr))
print(max(bingoList))