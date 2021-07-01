# 1041

n = int(input())
val = list(map(int, input().split()))
if n == 1 :
	print(sum(val) - max(val))
else:
	score = [min(val[0], val[-1]), min(val[1], val[-2]), min(val[2], val[-3])]
	score.sort()
	p3 = sum(score)
	p2 = p3 - score[2]
	print((n-2)*((n-2)*5+4)*score[0]+((n-2)*8+4)*p2+4*p3)

# 개선 전

# def checkNum(val, peice):
# 	vals = []
# 	vals.append(min(val[0], val[-1]))
# 	vals.append(min(val[1], val[-2]))
# 	vals.append(min(val[2], val[-3]))
# 	if peice == 2:
# 		return sum(vals) - max(vals)
# 	return sum(vals)


# n = int(input())
# val = list(map(int, input().split()))


# if n == 1 :
# 	print(sum(val) - max(val))
# else:
# 	score = []
# 	score.append((n - 2) * (n - 2) * 5 * min(val))
# 	score.append((n - 2) * 4 * min(val))
# 	score.append((n - 2) * 8 * checkNum(val, 2))
# 	score.append(4 * checkNum(val, 2))
# 	score.append(4 * checkNum(val, 3))

# 	print(sum(score))