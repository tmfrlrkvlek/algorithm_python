#1706

r, c = map(int, input().split())
s = 1
strList = []
order = []
for i in range(r):
	l = input()
	strList.append(l)
	l = l.split('#')
	for j in range(len(l)):
		if len(l[j]) < 2:
			continue
		order.append(l[j])

for i in range(c):
	l = ''
	for j in range(r):
		l += strList[j][i]
	l = l.split('#')
	for j in range(len(l)):
		if len(l[j]) < 2 :
			continue
		order.append(l[j])

order.sort()
print(order[0])