# 1105

l, r = input().split()
ll = list(l)
lr = list(r)

n = 0
if len(ll) != len(lr):
	print(0)

else:
	for i in range(len(str(l))) :
		if ll[i] == lr[i]:
			if ll[i] == '8':
				n+=1
		else:
			break

	print(n)