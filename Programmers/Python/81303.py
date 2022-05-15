def solution(n, k, cmds):
    def command(cmd) :
        if cmd[0] in ['U', 'D'] :
            a, b = map(str, cmd.split())
            return (a, int(b))
        else :
            return (cmd, 0)
        
    next_idxs = {}
    def find_next(idx) :
        if idx >= n-1 :
            return n
        elif idx in next_idxs :
            if next_idxs[idx] == n :
                return n
            elif exists[next_idxs[idx]] :
                return next_idxs[idx]
            else :
                next_idx = find_next(next_idxs[idx]) 
                next_idxs[idx] = next_idx
                return next_idx
        else :
            if exists[idx+1] :
                next_idxs[idx] = idx+1
                return idx+1
            else :
                next_idx = find_next(idx+1) 
                next_idxs[idx] = next_idx
                return next_idx
    
    before_idxs = {}
    def find_before(idx) :
        if idx < 1 :
            return -1
        elif idx in before_idxs :
            if before_idxs[idx] < 0 :
                return -1
            elif exists[before_idxs[idx]] :
                return before_idxs[idx]
            else :
                before_idx = find_before(before_idxs[idx])
                before_idxs[idx] = before_idx
                return before_idx
        else :
            if exists[idx-1] :
                before_idxs[idx] = idx-1
                return idx-1
            else :
                before_idx = find_before(idx-1)
                before_idxs[idx] = before_idx
                return before_idx
            
    def move(N, k) :
        if N < 0 :
            for _ in range(abs(N)) :
                k = find_before(k)
        elif N > 0 :
            for i in range(N):
                k = find_next(k)
        return k
    
    exists = [True] * n
    deletes = []
    N = 0
    for cmd in cmds :
        content, num = command(cmd)
        if content == 'D' :
            N += num
        elif content == 'U' :
            N -= num
        elif content == 'Z' :
            k = move(N, k)
            N = 0
            num = deletes.pop()
            exists[num] = True
            
            before_idx = find_before(num)
            next_idx = find_next(num)
            if before_idx >= 0 :
                next_idxs[before_idx] = num
            if next_idx < n :
                before_idxs[next_idx] = num
        else :
            k = move(N, k)
            N = 0
            deletes.append(k)
            exists[k] = False
            
            before_idx = find_before(k)
            next_idx = find_next(k)
            if before_idx >= 0 :
                next_idxs[before_idx] = next_idx
            if next_idx < n :
                before_idxs[next_idx] = before_idx
            
            k = next_idx if next_idx < n else before_idx
    return ''.join(['O' if i else 'X' for i in exists])