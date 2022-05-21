# 2559
n, k = map(int, input().split())
nums = list(map(int, input().split()))
current = sum(nums[:k])
result = current
for i in range(n-k) :
    current -= nums[i]
    current += nums[i+k]
    result = max(result, current)
print(result)