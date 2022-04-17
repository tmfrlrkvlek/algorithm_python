counts = {}

def solution(orders, course):
    [findCombis(''.join(sorted(list(order))), '', False, course) for order in orders]
    answer = {c: (2, []) for c in course}
    for key in counts :
        if len(key) in course :
            if answer[len(key)][0] < counts[key] : 
                answer[len(key)] = (counts[key], [key])
            elif answer[len(key)][0] == counts[key] :
                answer[len(key)][1].append(key)
    return sorted(sum([answer[key][1] for key in answer], []))


def findCombis(order, string, passable, courses):
    if (not passable) and len(string) in courses :
        counts[string] = 1 if string not in counts else counts[string]+1
    if len(order) :
        findCombis(order[1:], string, True, courses)
        findCombis(order[1:], string+order[0], False, courses)