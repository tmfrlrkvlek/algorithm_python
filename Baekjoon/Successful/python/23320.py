import sys
input = sys.stdin.readline
n = int(input())
s = list(map(int, input().split()))
r, ms = map(int, input().split())
print(n*r//100, len([True for i in s if i >= ms]))