import math

# mine
def sqrt2(num) :
    q = 0
    while num > 1 :
        num = int(num / 2)
        q += 1
    return q

n = int(input()) - 1
num = 0
while n != 0 :
    n -= 2 ** sqrt2(n)
    num += 1
print(num % 2)

# answer
# print(bin(int(input()) - 1).count('1') % 2)
