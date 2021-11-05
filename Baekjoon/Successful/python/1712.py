import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
print("-1" if c <= b else int(a/(c-b)+1))