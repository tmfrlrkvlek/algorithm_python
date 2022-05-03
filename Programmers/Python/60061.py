building = []
n = 0

def solution(N, build_frame):
    global building, n
    n = N
    building = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]

    for frame in build_frame :
        x, y, a, b = (frame[0], frame[1], frame[2], frame[3])
        if b == 0:
            building[x][y][a] = False
            if not (remove_pillar(x, y) if a == 0 else remove_bo(x, y)) :
                building[x][y][a] = True
        else :
            if build_pillar(x, y) if a == 0 else build_bo(x, y) :
                building[x][y][a] = True
    answer = []
    [[[answer.append([i, j, k]) for k in range(2) if building[i][j][k]] for j in range(n+1)] for i in range(n+1)]
                    
    return answer

def build_pillar(x, y) :
    if y == 0 :
        return True
    elif y > 0 and building[x][y-1][0]:
        return True
    elif x > 0 and building[x-1][y][1] :
        return True
    elif building[x][y][1] :
        return True
    else :
        return False

def build_bo(x, y) :
    if y > 0 and building[x][y-1][0] :
        return True
    elif y > 0 and x < n and building[x+1][y-1][0] :
        return True
    elif 0 < x < n and building[x+1][y][1] and building[x-1][y][1]:
        return True
    else :
        return False
        
def remove_pillar(x, y) :
    if y < n and building[x][y+1][0] and not build_pillar(x, y+1) :
        return False
    elif x > 0 and building[x-1][y+1][1] and not build_bo(x-1, y+1) :
        return False
    elif building[x][y+1][1] and not build_bo(x, y+1) :
        return False
    else : 
        return True
    
def remove_bo(x, y) :
    if building[x][y][0] and not build_pillar(x, y) :
        return False
    elif x < n and building[x+1][y][0] and not build_pillar(x+1, y) :
        return False
    elif x < n and building[x+1][y][1] and not build_bo(x+1, y) :
        return False
    elif x > 0 and building[x-1][y][1] and not build_bo(x-1, y) :
        return False
    else :
        return True