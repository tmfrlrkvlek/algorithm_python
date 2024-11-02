# 10709

h, w = map(int, input().split())
for i in range(h) : 
    skyline = input()
    minutes = -1
    for j in range(w) :
        if skyline[j] == 'c' :
            minutes = 0
        elif minutes >= 0 :
            minutes += 1
        print(minutes, end=" ")
    print()

