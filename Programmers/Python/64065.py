def solution(s):
    s = "".join(list(s)[2:-2])
    ss = s.split("},{")
    tuple = []
    for item in sorted(ss, key=lambda x: len(x)) :
        [tuple.append(num) for num in list(map(int, item.split(","))) if num not in tuple]
    return tuple

def solution2(s):
    s = sorted(s[2:-2].split('},{'), key=lambda x: len(x))
    answer = []
    [[answer.append(num) for num in list(map(int, str.split(','))) if num not in answer] for str in s]
    return answer