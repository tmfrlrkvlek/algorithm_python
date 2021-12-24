# 1878
# https://programmers.co.kr/learn/courses/18/lessons/1878?language=python3

def solution(v) :
	answer = []
	x = []
	y = []
	for k in v :
		x.append(k[0])
		y.append(k[1])
	for i in x :
		if x.count(i) == 1 :
			answer.append(i)
			break
	for i in y :
		if y.count(i) == 1 :
			answer.append(i)
			break
	return answer