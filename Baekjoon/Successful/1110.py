# 1110

num = int(input())
num2 = num
time = 0

while(1):
    time += 1
    n10 = num2 % 10
    n1 = (num2 // 10 + n10) % 10
    num2 = n10 * 10 + n1
    if num == num2:
        break
print(time)