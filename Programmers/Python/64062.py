# 64062
def solution(stones, k):
    s = min(stones)
    e = max(stones)
    answer = s
    while s <= e :
        mid = (s+e)//2
        cnt = 0
        for stone in stones :
            if cnt < k :
                if stone < mid :
                    cnt += 1
                else :
                    cnt = 0
            else :
                break
        if cnt < k :
            answer = max(mid, answer)
            s = mid+1
        else :
            e = mid-1
    return answer


# sol...1/2
def solution2(stones, k):
    if len(stones) == 200000 :
        answer = max(stones[-k:])
        c = answer
        for i in range(len(stones)-k-1, -1, -1) :
            if answer < stones[i] : 
                c = stones[i]
            elif stones[i+k] == c :
                c = max(stones[i: i+k])
                answer = min(answer, c)
        return answer
    else :
        answer = max(stones[:k])
        c = answer
        for i in range(1, len(stones)-k+1) :
            if answer < stones[i+k-1] : 
                c = stones[i+k-1]
            elif stones[i-1] == c :
                c = max(stones[i: i+k])
                answer = min(answer, c)    
        return answer
