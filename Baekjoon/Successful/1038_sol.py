#1038

def resfunc(n, sum, res):
	if n == -1:
		res.append(sum)
		return
	resfunc(n - 1, sum, res)
	resfunc(n - 1, (sum * 10) + n, res)

res = []
n = int(input())

if n >= 1023 :
	print(-1)

else :
	resfunc(9, 0, res)
	res.sort()
	print(res[n+1])