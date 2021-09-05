l = [0] * 10
a = int(input())
a *= int(input())
a *= int(input())

while (a > 0):
    l[a % 10] += 1
    a = a // 10

for value in l:
    print(value)