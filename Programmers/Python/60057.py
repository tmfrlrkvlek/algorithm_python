def solution(s):
    result = len(s)
    for c in range(1, len(s)//2+1) :
        result = min(length(s, c), result)
    return result

def length(s, c):
    start = 0
    length = len(s)
    accCnt = 1
    for start in range(c, len(s), c) :
        if s[start-c:start] == s[start:start+c] :
            accCnt += 1
        else :
            if accCnt > 1 :length -= (c*(accCnt-1) - len(str(accCnt)))
            accCnt = 1
    return length if accCnt == 1 else length - (c*(accCnt-1) - len(str(accCnt)))
        