from itertools import combinations as cb

def solution(orders, course) :
    courses = {}
    for order in orders: 
        order = sorted(order)
        for c_cnt in course :
            for combi in cb(order, c_cnt) :
                c1 = ''.join(combi)
                if c1 in courses :
                    courses[c1] += 1
                else :
                    courses[c1] = 1
    result = {cnt: ([], 0) for cnt in course}
    for course, cnt in courses.items() :
        length = len(course)
        if result[length][1] < cnt :
            result[length] = ([course], cnt)
        elif result[length][1] == cnt :
            result[length][0].append(course)
    return sorted(sum([re[0] for _, re in result.items() if re[1] > 1], []))

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))