x, y, w, h = input().split()
x = int(x)
y = int(y)
w = int(w)
h = int(h)

d1 = abs(x - w)
d2 = abs(y - h)
d3 = abs(0 - x)
d4 = abs(0 - y)

print(min(d1, d2, d3, d4))

# 11111111
# 1      1  
# 1      1
# 1      1
# 11111111