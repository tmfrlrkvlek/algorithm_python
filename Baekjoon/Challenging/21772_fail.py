# def selectMax(step, maxx, maxy, loc, rootList):
# 	global gmap
# 	global rmap
	
# 	if loc[0] >= maxy or loc[0] < 0 or loc[1] >= maxy or loc[1] < 0:
# 		return -1
# 	elif rmap[loc[0]][loc[1]] == '#' :
# 		return -1
# 	elif step == 0:
# 		return max(
# 					selectMax(step + 1, maxx, maxy, [loc[0],loc[1]+1], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0],loc[1]-1,], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0]+1,loc[1]], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0]-1,loc[1]], rootList)
# 					)

# 	maxVal = 0
# 	maxVal = max(
# 		gmap[loc[0]][loc[1]+1],gmap[loc[0]][loc[1]-1],
# 		gmap[loc[0]+1][loc[1]],gmap[loc[0]-1][loc[1]])
# 	if rmap[loc[0]][loc[1]] == 'S' and (loc[0]*maxy + loc[1]) not in rootList:
# 		rootList.append(loc[0]*maxy + loc[1])
# 		gmap[loc[0]][loc[1]] = maxVal + 1
# 		print(gmap)
# 	else:
# 		gmap[loc[0]][loc[1]] = maxVal
	
# 	if step == maxx:
# 		return gmap[loc[0]][loc[1]]
# 	else:
# 		return max(
# 					selectMax(step + 1, maxx, maxy, [loc[0],loc[1]+1], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0],loc[1]-1,], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0]+1,loc[1]], rootList),
# 					selectMax(step + 1, maxx, maxy, [loc[0]-1,loc[1]], rootList)
# 					)

# r, c, t = map(int, input().split())
# gmap = []
# rmap = []

# loc = [0, 0]
# for i in range(r):
# 	rmap.append(list(input()))
# 	gmap.append([0] * (r+1))
# 	if 'G' in rmap[i]:
# 		loc[0] = i
# 		loc[1] = rmap[i].index('G')

# gmap.append([0] * (r+1))
# rootList = []
# print(selectMax(0, t, r, loc, rootList))

# print(gmap)