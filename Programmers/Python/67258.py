def solution(gems):
    counts = {g: 0 for g in list(set(gems))}
    answer = [0, len(gems)-1]
    l = 0
    r = 0
    gems.append(gems[0])
    counts[gems[0]] += 1
    buyable = buy(counts)
    while r < len(gems)-1 and l <= r :
        if buyable :
            if r-l < answer[1] - answer[0] :
                answer = [l, r]
            counts[gems[l]] -= 1
            if counts[gems[l]] == 0 : 
                buyable = buy(counts)
            l += 1
        else :
            r += 1
            counts[gems[r]] += 1
            if counts[gems[r]] == 1 :
                buyable = buy(counts)
    return [answer[0]+1, answer[1]+1]

def buy(counts) :
    for _, item in counts.items():
        if item == 0 : return False
    return True