# 20548

# import math
# n = int(input())
# i = 1
# while n >= (7**i) : i += 1
# l = []
# for i in range(i - 1, -1, -1) :
#     l.append(min(math.floor(n/(7**i)), 2))
#     n -= 7**i*l[-1]
# index = 0
# for i, n in enumerate(l) :
#     index += 3**(len(l) - i - 1)*n
# print(index)

n = int(input())
i, s = 13, ""
while i >= 0:
    t, n = divmod(n, 7 ** i)
    s += str(t)
    i -= 1
print(int(s,3))

