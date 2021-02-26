# https://codeforces.com/problemset/problem/1295/A

# 1->2
# 7->3
# 9->6

t = int(input())
while(t) :
    t -= 1
    n = int(input())
    num = [0,0,0,0,0,0,0,0,0,0]
    n10 = int(n / 2)
    total = 0
    if n10 > 10 :
        number = n % 20 
        n10 = 10
    else :
        number = n % 2
    while(n10) :
        n10 -= 1
        if (number >= 4):
            num[n10] = 9
            number -= 4
        elif(number >= 1):
            num[n10] = 7
            number -= 1
        else:
            num[n10] = 1
        total = (total * 10) + num[n10]
    print(total)
