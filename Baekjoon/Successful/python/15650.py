n, m = map(int, input().split())

def permutation(remainder, current, goal_count) :
    if len(current) == goal_count :
        print(" ".join(list(map(str, current))))
        return
    elif len(remainder) == 0 :
        return
    else :
        for idx in range(len(remainder)):
            permutation(
                remainder[idx+1:],
                current + [remainder[idx]],
                goal_count
            )

permutation([i for i in range(1, n+1)], [], m)