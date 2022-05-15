# 2784
import sys
from itertools import combinations as cb
from itertools import permutations as pm

def check(cube) :
    return sorted(list(cube) + [''.join([cube[j][i] for j in range(3)]) for i in range(3)]) == words

words = [sys.stdin.readline().strip() for _ in range(6)]
result = sorted(sum([['\n'.join(cube) for cube in pm(lines) if check(cube)] for lines in cb(words, 3)], []))
if result :
    print(result[0])
else :
    print(0)


# abc
# def
# ghi
# adg
# beh
# cfi