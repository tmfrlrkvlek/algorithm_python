n = int(input())
value = list(map(int, input().split()))
sum = [max(0, value[0])]
for i in range(1, n): sum.append(max(0, value[i] + sum[i - 1]))
if max(sum) : print(max(sum))
else : print(max(value))