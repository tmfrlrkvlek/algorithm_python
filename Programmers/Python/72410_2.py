def solution(new_id):
    id = new_id
    for idx in range(len(id)) :
        if 'A' <= id[idx] <= 'Z' :
            id = id[:idx] + chr(ord(id[idx])+32) + id[idx+1:]
    new_id = ''
    for c in id :
        if 'a' <= c <= 'z' :
            new_id += c
        elif '0' <= c <= '9' :
            new_id += c
        elif c in ['-', '_', '.'] :
            new_id += c
    id = '.'.join(filter(lambda x: len(x), new_id.split('.')))
    if len(id) > 0 and id[0] == '.' :
        id = id[1:]
    if len(id) > 0 and id[-1] == '.' :
        id = id[:-1]
    if len(id) == 0 :
        id = 'a'
    elif len(id) >= 16 :
        id = id[:15]
    if len(id) > 0 and id[-1] == '.' :
        id = id[:-1]
    for _ in range(len(id), 3) :
        id += id[-1]
    return id
print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))
