def solution(id_list, report, k):
    declaration = {id: set() for id in id_list}
    for re in report :
        declared, reported = map(str, re.split())
        declaration[declared].add(reported)
    counts = {id: 0 for id in id_list}
    for de in declaration:
        for p in list(declaration[de]) : counts[p]+=1
    stoppedUser = set()
    [stoppedUser.add(p) for p in counts if counts[p] >= k]
    return [len(declaration[id] & stoppedUser) for id in id_list]