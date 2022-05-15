# 정확성만 맞음

def solution(n, k, cmds):
    def command(cmd) :
        if cmd[0] in ['U', 'D'] :
            a, b = map(str, cmd.split())
            return (a, int(b))
        else :
            return (cmd, 0)
    def find_idx(num, table) :
        l = 0
        r = len(table)-1
        result = 0
        while l <= r:
            mid = (l+r)//2
            if table[mid] > num :
                result = mid
                l = mid+1
            else :
                r = mid-1
        return result
    table = [i for i in range(n)]
    deletes = []
    N = 0
    for cmd in cmds :
        content, num = command(cmd)
        if content == 'D' :
            k += num
        elif content == 'U' :
            k -= num
        elif content == 'Z' :
            num = deletes.pop()
            idx = find_idx(num, table)
            idx = idx+1 if table[idx] < num else idx
            table.insert(idx, num)
            if idx <= k : 
                k += 1
        else :
            deletes.append(table[k])
            del table[k]
            if k == len(table) :
                k -= 1
    exists = [False] * n
    for i in table :
        exists[i] = True
    return ''.join(['O' if i else 'X' for i in exists])
