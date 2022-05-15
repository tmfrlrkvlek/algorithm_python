# 72412

## 정확성 O 효율성 X
import re

def solution(info, querys):
    def info_to_string(info) :
        info = info.split()
        grade = int(info[-1])
        return (''.join([i[0] for i in info[:4]]), grade)
    
    def query_to_string(query) :
        query = query.split(' and ')
        query[-1], num_min = query[-1].split()
        num_min = int(num_min) 
        return (''.join(q[0] if q[0] != '-' else '.' for q in query), num_min)
    
    def find(query) :
        key = query.replace('.', '')
        if query in dp :
            return dp[query]
        elif len(key) == 1 :
            dp[query] = count(query)
        else :
            for i in range(4) :
                if query[i] != '.' :
                    dp[query] = find(query[:i+1]+'.'*(4-i-1)) & find('.'*(i+1)+query[i+1:])
                    break
        return dp[query]
    
    def count(query) :
        answer = set()
        q = re.compile(query)
        for idx in range(len(infos)) :
            if re.match(q, infos[idx][0]) != None :
                answer.add(idx)
        return answer
    
    dp = {}
    dp['....'] = set([i for i in range(len(info))])
    infos = [info_to_string(i) for i in info]
    querys = [query_to_string(q) for q in querys]
    for a in ['.', 'j', 'p', 'c'] :
        for b in ['.', 'b', 'f'] :
            for c in ['.', 'j', 's'] :
                for d in ['.', 'p', 'c'] :
                    find(f"{a}{b}{c}{d}")
        
    return [len([i for i in list(dp[query[0]]) if infos[i][1] >= query[1]]) for query in querys]

print(solution(["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"], ["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]))



import re

def solution2(info, querys):
    dp = {}
    
    def info_to_string(info) :
        info = info.split()
        grade = int(info[-1])
        return (''.join([i[0] for i in info[:4]]), grade)
    
    def query_to_string(query) :
        query = query.split(' and ')
        query[-1], num_min = query[-1].split()
        num_min = int(num_min) 
        return (''.join(q[0] if q[0] != '-' else '.' for q in query), num_min)
    
    def count(query, infos) :
        answer = []
        if query[0] in dp :
            answer = dp[query[0]]
        else :
            q = re.compile(query[0])
            for info, grade in infos :
                if re.match(q, info) != None :
                    answer.append(grade)
            dp[query[0]] = answer
        return len([False for i in answer if i >= query[1]])
    
    info = [info_to_string(i) for i in info]
    querys = [query_to_string(q) for q in querys]
    return [count(query, info) for query in querys]