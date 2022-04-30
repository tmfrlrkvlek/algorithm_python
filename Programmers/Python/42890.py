def solution(relation):
    return len(bfs(relation, list(range(len(relation[0])))))
    
def bfs(relation, rows) :
    if not isKey(relation, rows) : return []
    else :
        answer = [] 
        for i in range(len(rows)):
            result = bfs(relation, rows[:i]+rows[i+1:])
            [answer.append(row) for row in result if row not in answer]
        if not answer : return [rows]
        else : return answer

def isKey(relation, rows) :
    infos = [''.join([rel[row] for row in rows]) for rel in relation]
    return len(set(infos)) == len(infos)