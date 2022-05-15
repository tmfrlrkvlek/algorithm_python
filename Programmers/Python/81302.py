import re

def solution(places):
    answer = []
    def satisfy(place):
        cases = [re.compile(string) for string in ['PP', 'POP', 'PO.....P', 'P.....OP', 'OP....P.', '.P....PO']]
        
        line = ' '.join(place)
        for case in cases:
            if re.search(case, line) :
                return False
        line = ' '.join([''.join([i[j] for i in place]) for j in range(5)])
        for case in cases:
            if re.search(case, line) :
                return False
        return True
    return [1 if satisfy(place) else 0 for place in places]