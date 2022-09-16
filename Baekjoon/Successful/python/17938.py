# 17938
import sys
input = sys.stdin.readline

def solve():
    N = int(input().strip())
    P, T = map(int, input().strip().split())
    ps = [0, 0]
    turn = 0
    increase = True
    for _ in range(T):
        if increase and turn < 2*N :
            turn += 1
        else :
            turn -= 1
        if turn == 1 :
            increase = True
        elif turn == 2*N :
            increase = False
        right = ps[1]
        ps = [i if i > 0 else 2*N for i in [(right+1)%(2*N), (right+turn)%(2*N)]]
    
    left, right = ps
    hands = None
    if left <= right :
        hands = set(list(range(left, right+1)))
    else :
        hands = set(list(range(left, 2*N+1)) + list(range(1, right+1)))

    hs = set([P*2-1, P*2])
    if hs & hands and hands - hs:
        print("Dehet YeonJwaJe ^~^")
    else :
        print("Hing...NoJam")
solve()