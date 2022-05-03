# 67256

# sol1
def solution(numbers, hand):
    priority = 0 if hand == "left" else 1
    numbers = [num if num != 0 else 11 for num in numbers]
    p = [10, 12]
    answer = ''
    for num in numbers :
        n = num % 3 
        if n == 1 : p[0] = num; answer+='L'
        elif n == 0 : p[1] = num; answer+='R'
        else : 
            pos = closer(diff(num, p[0]), diff(num, p[1]), priority)
            p[pos] = num; answer+='L' if pos == 0 else 'R'
    return answer

def diff(num, p) :
    num -= 1; p -= 1
    return abs(num//3-p//3) + abs(p%3-num%3)

def closer(a, b, d) :
    if a != b : return 0 if a < b else 1
    else : return d

# sol2
hands = [10, 12]

def solution(numbers, hand):
    side = 0 if hand == "left" else 1
    result = ""
    for num in numbers :
        if num == 0 : num = 11
        if finger(num, side) :
            result += "L"
            hands[0] = num
        else :
            result += "R"
            hands[1] = num
    return result

def finger(num, side) :
    if num in [1, 4, 7] :
        return True
    elif num in [3, 6, 9] :
        return False
    else :
        ld = distance(num, hands[0])
        rd = distance(num, hands[1])
        if ld > rd :
            return False
        elif ld == rd :
            return False if side else True
        else :
            return True
            
def distance(n1, n2) :
    return abs(n1-n2) // 3 + abs(n1-n2) % 3