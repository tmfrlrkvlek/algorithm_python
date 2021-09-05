# 1495
def checkVolume(alist, idx):
	global vlist, m, n
	klist = []

	for i in alist:
		num = i + vlist[idx]
		if num <= m and num not in klist:
			klist.append(num)
		num = i - vlist[idx]
		if num >= 0 and num not in klist:
			klist.append(num)

	if idx + 1 == n :
		if not klist:
			return -1
		else:
			return max(klist)

	else : 
		return checkVolume(klist, idx + 1)
		
n, s, m = map(int, input().split())
vlist = list(map(int, input().split()))
print(checkVolume([s], 0))