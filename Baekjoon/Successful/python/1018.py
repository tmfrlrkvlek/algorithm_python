# 1018

m, n = map(int, input().split())
white = []
for i in range(m) :
    line = []
    l = list(input())
    for j in range(n) :
        line.append(1 if ((i + j) % 2) == (l[j] == 'W') else 0)
    white.append(line)
nums = []
for i in range(m - 8 + 1):
    for j in range(n - 8 + 1):
        nums.append(sum(sum([row[j:j+8] for row in white[i:i+8]], [])))
        nums.append(64 - nums[-1])
print(min(nums))