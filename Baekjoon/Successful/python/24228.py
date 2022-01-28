# 24228
import sys
n, r = map(int, sys.stdin.readline().strip().split())
print(n+2*(r-1)+1)

# 3
# abc
# 4
# abca -> 1
# 5
# abcaa -> 1
# 6
# abcaab -> 2
# 7
# abcaabb -> 2
# 8
# abcaabba -> 3
# 9
# abcaabbaa -> 3
# 10
# abcaabbaac -> 3