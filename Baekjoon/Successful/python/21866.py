# 21866

def isHacker(s, l) :
    for i in range(0, 9):
        if s[i] > l[i] : return True
    return False

l = [100, 100, 200, 200, 300, 300, 400, 400, 500]
s = list(map(int, input().split()))
if sum(s) < 100 :
    print("none")
elif isHacker(s, l) :
    print("hacker")
else :
    print("draw")
