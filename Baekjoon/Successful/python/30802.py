n = int(input())
counts = list(map(int, input().split()))
t, p = map(int, input().split())

result = 0
for count in counts :
    result += count // t
    result += 1 if count % t > 0 else 0
print(result)
print(n // p, n % p)