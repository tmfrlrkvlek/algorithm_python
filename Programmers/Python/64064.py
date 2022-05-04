# 64064

def solution(user_id, banned_id):
    answer = 1
    banned_ids = [banned_id_list(user_id, id) for id in banned_id]
    return len(set(count(banned_ids, [], len(user_id))))

def banned_id_list(user_id, banned_id) :
    result = []
    for id in range(len(user_id)) :
        if len(user_id[id]) != len(banned_id) : 
            continue
        isFit = True
        for idx in range(len(banned_id)) :
            if banned_id[idx] != "*" and banned_id[idx] != user_id[id][idx] :
                isFit = False
                break
        if isFit : result.append(id)
    return result

def count(banned_ids, current, n) :
    if not banned_ids : 
        result = ['0'] * n
        for i in current:
            result[i] = '1'
        return [''.join(result)]
    id_array = [id for id in banned_ids[0] if id not in current]
    if not id_array :
        return []
    else :
        currents = []
        for id in id_array :
            result = count(banned_ids[1:], current+[id], n)
            if result : currents.append(result)
        return sum(currents, [])