def solution(key, lock):
    for _ in range(4) :
        if openAvailable(key, lock) : return True
        key = rotate(key)
    return False

def rotate(key):
    key2 = [[] for _ in range(len(key))]
    for row in key :
        for col in range(len(key)) :
            key2[col].append(row[col])
    return [row[::-1] for row in key2]
        
def openAvailable(key, lock) :
    for i in range(-len(lock)+1, len(lock)) :
        for j in range(-len(lock)+1, len(lock)) :
            if correct(key, lock, i, j) : return True
            
def correct(key, lock, x, y) :
    for i in range(len(lock)) :
        for j in range(len(lock)) :
            if lock[i][j] == 0 :
                if 0 <= i-x < len(key) and 0 <= j-y < len(key) and key[i-x][j-y] == 1 :
                    continue
                else :
                    return False
            else :
                if 0 <= i-x < len(key) and 0 <= j-y < len(key) and key[i-x][j-y] == 1 :
                    return False
    return True